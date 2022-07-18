from django.db import models


class Orders(models.Model):
    sequence_number = models.IntegerField(verbose_name='Порядковый номер')
    order_number = models.BigIntegerField(verbose_name='Номер заказа')
    cost_in_dollars = models.FloatField(verbose_name='Стоимость в долларах')
    cost_in_rubles = models.FloatField(verbose_name='Стоимость в рублях')
    delivery_time = models.DateField(verbose_name='Срок поставки')

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'


class ExchangeRate(models.Model):
    date_time = models.DateTimeField(verbose_name='Время получения курса')
    exchange_rate = models.FloatField(verbose_name='Курс рубля к доллару')

    class Meta:
        verbose_name = 'Курс доллара'
        verbose_name_plural = 'Курсы доллара'

    def __str__(self) -> str:
        return str(self.exchange_rate)
