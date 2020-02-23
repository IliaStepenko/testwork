from currencylist.models import ExchangeRate, CurrencyDictionary
from django.db.models import Count, Max
from django.test import TestCase
import datetime


class ExchangeRateModelTest(TestCase):

    def setUp(self):
        self.currency = CurrencyDictionary.objects.create(full_name='United States Dollar', code='USD')

        ExchangeRate.objects.bulk_create([
            ExchangeRate(purchase=24.45, sale=24.95, currency=self.currency,
                         start_date=datetime.date(2019, 12, 30), end_date=datetime.date(2019, 1, 2)),
            ExchangeRate(purchase=24.15, sale=24.55, currency=self.currency,
                         start_date=datetime.date(2020, 1, 3), end_date=datetime.date(2020, 1, 14)),
            ExchangeRate(purchase=24.15, sale=24.45, currency=self.currency,
                         start_date=datetime.date(2020, 1, 15), end_date=datetime.date(2020, 1, 17)),
            ExchangeRate(purchase=292.45, sale=243.95, currency=self.currency,
                         start_date=datetime.date(2018, 10, 2), end_date=datetime.date(2018, 10, 5)),
            ExchangeRate(purchase=243.15, sale=24.55, currency=self.currency,
                         start_date=datetime.date(2018, 10, 10), end_date=datetime.date(2018, 10, 15)),
            ExchangeRate(purchase=229.15, sale=24.55, currency=self.currency,
                         start_date=datetime.date(2018, 10, 16), end_date=datetime.date(2018, 10, 19))])

    def test_inside_interval_insertion(self):
        testing_object = ExchangeRate(
            purchase=23.15,
            sale=13.29,
            currency=self.currency,
            start_date=datetime.date(2020, 1, 10)
        )
        testing_object.save()
        self.assertEqual(testing_object.end_date, datetime.date(2020, 1, 14))

    def test_deletion(self):
        testing_object = ExchangeRate.objects.filter(start_date=datetime.date(2020, 1, 3)).first()
        testing_object.delete()
        testing_object = ExchangeRate.objects.filter(start_date=datetime.date(2019, 12, 30)).first()

        self.assertEqual(testing_object.end_date, datetime.date(2020, 1, 14))

    def test_insert_between_interval(self):
        test_object = ExchangeRate(purchase=292.45, sale=243.95, currency=self.currency,
                                   start_date=datetime.date(2018, 10, 7))
        test_object.save()
        self.assertEqual(test_object.end_date, datetime.date(2018, 10, 9))

    def test_insert_at_start(self):
        test_object = ExchangeRate(purchase=292.45, sale=243.95, currency=self.currency,
                                   start_date=datetime.date(2018, 9, 29))
        test_object.save()
        self.assertEqual(test_object.end_date, datetime.date(2018, 10, 1))

    def test_insert_at_end(self):
        test_object = ExchangeRate(purchase=292.45, sale=243.95, currency=self.currency,
                                   start_date=datetime.date(2018, 10, 21))
        test_object.save()
        test_object = ExchangeRate.objects.filter(purchase=229.15).first()
        self.assertEqual(test_object.end_date, datetime.date(2018, 10, 20))
