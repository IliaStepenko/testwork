from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator
from django.db import models
import datetime


class CurrencyDictionary(models.Model):
    full_name = models.CharField(max_length=80)
    code = models.CharField(max_length=10)


class ExchangeRate(models.Model):
    purchase = models.FloatField(validators=[MinValueValidator(0), ])
    sale = models.FloatField(validators=[MinValueValidator(0), ])
    currency = models.ForeignKey(CurrencyDictionary, on_delete=models.CASCADE)
    start_date = models.DateField(default=datetime.date.today, blank=True)
    end_date = models.DateField(default=None, blank=True, null=True)

    def save(self, create_children=True, **kwargs):
        if create_children and not self.pk:

            editable_date = ExchangeRate.objects.filter(currency=self.currency,
                                                        start_date__lte=self.start_date,
                                                        end_date__gte=self.start_date)
            if editable_date:
                editable_date = editable_date.first()
                self.end_date = editable_date.end_date
                editable_date.end_date = self.start_date - datetime.timedelta(days=1)
                editable_date.save(update_fields=['end_date'])
                result = super(ExchangeRate, self).save(**kwargs)
                return result

            editable_date = ExchangeRate.objects.filter(currency=self.currency,
                                                        start_date__gt=self.start_date
                                                        ).order_by('start_date')

            if editable_date:
                editable_date = editable_date.first()
                self.end_date = editable_date.start_date - datetime.timedelta(days=1)

            editable_date = ExchangeRate.objects.filter(currency=self.currency,
                                                        end_date__lt=self.start_date
                                                        ).order_by('end_date')

            if editable_date:
                editable_date = editable_date.last()

                editable_date.end_date = self.start_date - datetime.timedelta(days=1)
                editable_date.save(update_fields=['end_date'])

            super(ExchangeRate, self).save(**kwargs)


        else:
            super(ExchangeRate, self).save(**kwargs)

    def delete(self, *args, **kwargs):
        record_for_replace = ExchangeRate.objects.filter(end_date__lt=self.start_date).order_by('end_date').last()
        record_for_replace.end_date = self.end_date
        record_for_replace.save(update_fields=['end_date'])
        super(ExchangeRate, self).delete()
