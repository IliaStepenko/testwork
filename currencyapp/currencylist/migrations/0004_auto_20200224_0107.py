# Generated by Django 3.0.3 on 2020-02-23 19:59
import datetime
from random import randint

from django.db import migrations


def fill_data(apps, schema_editor):
    currency = apps.get_model('currencylist', 'CurrencyDictionary')
    exchange_rate = apps.get_model('currencylist', 'ExchangeRate')

    usd = currency.objects.create(full_name="United States Dollar", code="USD")
    gbp = currency.objects.create(full_name="Pound sterling", code="GBP")
    rub = currency.objects.create(full_name="Российский рубль", code="RUB")
    eur = currency.objects.create(full_name="Euro", code="EUR")
    pln = currency.objects.create(full_name="Polish złoty", code="PLN")
    chf = currency.objects.create(full_name="Swiss franc", code="CHF")

    exchange_rate.objects.bulk_create([
        exchange_rate(purchase=24.45, sale=24.95, currency=usd,
                      start_date=datetime.date(2019, 12, 30), end_date=datetime.date(2019, 1, 2)),
        exchange_rate(purchase=24.15, sale=24.55, currency=usd,
                      start_date=datetime.date(2020, 1, 3), end_date=datetime.date(2020, 1, 14)),
        exchange_rate(purchase=24.15, sale=24.45, currency=usd,
                      start_date=datetime.date(2020, 1, 15), end_date=datetime.date(2020, 1, 17))
    ])

    interval_start_date = datetime.date(2020, 2, 13)
    interval_end_date = datetime.date(2020, 2, 16)

    for i in range(1, 15, 1):
        exchange_rate.objects.bulk_create([
            exchange_rate(purchase=24.45 + randint(0, 10), sale=24.95 + randint(0, 10), currency=usd,
                          start_date=interval_start_date, end_date=interval_end_date),
            exchange_rate(purchase=24.45 + randint(0, 10), sale=24.95 + randint(0, 10), currency=gbp,
                          start_date=interval_start_date, end_date=interval_end_date),
            exchange_rate(purchase=24.45 + randint(0, 10), sale=24.95 + randint(0, 10), currency=rub,
                          start_date=interval_start_date, end_date=interval_end_date),
            exchange_rate(purchase=24.45 + randint(0, 10) , sale=24.95 + randint(0, 10), currency=eur,
                          start_date=interval_start_date, end_date=interval_end_date),
            exchange_rate(purchase=24.45 + randint(0, 10), sale=24.95 + randint(0, 10), currency=pln,
                          start_date=interval_start_date, end_date=interval_end_date),
            exchange_rate(purchase=24.45 + randint(0, 10), sale=24.95 + randint(0, 10), currency=chf,
                          start_date=interval_start_date, end_date=interval_end_date)
        ])

        interval_start_date = interval_end_date + datetime.timedelta(days=1)
        interval_end_date = interval_start_date + datetime.timedelta(days=3)


class Migration(migrations.Migration):
    dependencies = [
        ('currencylist', '0003_auto_20200223_2117'),
    ]

    operations = [
        migrations.RunPython(fill_data),
    ]