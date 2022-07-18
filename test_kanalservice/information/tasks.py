import datetime
import os

import gdown
import pandas as pd
import requests
import xmltodict
from celery import shared_task
from django.db.models import Sum
from telegram import Bot

from information.models import ExchangeRate, Orders


@shared_task
def save_exchange_rate():
    """ Функция добывает значение курса доллара на текущую дату и сохраняет его
    """
    url = 'https://www.cbr.ru/scripts/XML_daily.asp'
    response = requests.get(url)
    exchange_dict = xmltodict.parse(response.text)
    exchange_list = exchange_dict.get('ValCurs').get('Valute')
    for elem in exchange_list:
        if elem.get('CharCode') == 'USD':
            rate = ExchangeRate.objects.create(
                exchange_rate=float(elem.get('Value').replace(',', '.')),
                date_time=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            )
            rate.save()
            break


@shared_task
def save_gdoc_data():
    """ Функция скачивает Google Sheets таблицу и обновляет данные в БД
    """
    data_dict = {}
    url = 'https://docs.google.com/uc?id=1jQb-XaDfeQmfB5LazkfXhY6uy3KFt3Ld'
    output = 'fyle.xlsx'
    gdown.download(url, output, quiet=True)

    excel_data = pd.read_excel('fyle.xlsx')
    os.remove(output)
    for data in excel_data.to_dict(orient='records'):
        data_dict[data.get(tuple(data.keys())[0])] = (
            data.get(tuple(data.keys())[1]),
            data.get(tuple(data.keys())[2]),
            data.get(tuple(data.keys())[3]),
        )
    for key, value in data_dict.items():
        order, _ = Orders.objects.update_or_create(
            order_number=value[0],
            defaults={
                'sequence_number': key,
                'cost_in_dollars': value[1],
                'delivery_time': value[2],
                'cost_in_rubles': (
                    value[1] * ExchangeRate.objects.last().exchange_rate
                )
            }
        )
        order.save()


@shared_task
def send_message():
    """ Функция отправляет в телеграмм сообщение о просроченных заказах
    """
    overdue_orders = Orders.objects.filter(delivery_time__lt=datetime.date.today())
    money_for_overdue_orders = overdue_orders.aggregate(Sum('cost_in_dollars'))
    sum_in_dollars = list(money_for_overdue_orders.values())[0]
    bot = Bot(token=os.environ.get('TOKEN', ''))
    chat_id = os.environ.get('CHAT_ID', False)
    text = f'Просрочено {overdue_orders.count()} заказов на сумму {sum_in_dollars}$'
    bot.send_message(chat_id, text)
