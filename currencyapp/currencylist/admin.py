from django.contrib import admin
from currencylist.models import ExchangeRate, CurrencyDictionary


# Register your models here.
admin.site.register(ExchangeRate)
admin.site.register(CurrencyDictionary)