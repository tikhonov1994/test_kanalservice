# Generated by Django 4.0.6 on 2022-07-16 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ExchangeRate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_time', models.DateTimeField(verbose_name='Время получения курса')),
                ('exchange_rate', models.FloatField(verbose_name='Курс рубля к доллару')),
            ],
            options={
                'verbose_name': 'Курс доллара',
                'verbose_name_plural': 'Курсы доллара',
            },
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sequence_number', models.IntegerField(verbose_name='Порядковый номер')),
                ('order_number', models.BigIntegerField(verbose_name='Номер заказа')),
                ('cost_in_dollars', models.FloatField(verbose_name='Стоимость в долларах')),
                ('cost_in_rubles', models.FloatField(verbose_name='Стоимость в рублях')),
                ('delivery_time', models.DateField(verbose_name='Срок поставки')),
            ],
            options={
                'verbose_name': 'Заказ',
                'verbose_name_plural': 'Заказы',
            },
        ),
    ]
