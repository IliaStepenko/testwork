import datetime

from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from django.views.generic import ListView

from currencylist.models import ExchangeRate


class ActualExchangeRate(ListView):

    template_name = 'currency_list.html'
    context_object_name = 'exchange_rate_model'
    queryset = ExchangeRate.objects.filter(start_date__lte=datetime.date.today(), end_date__gte=datetime.date.today())

    def get_context_data(self, **kwargs):
        context = super(ActualExchangeRate, self).get_context_data(**kwargs)
        context['page_title'] = 'Actual exchange rate'
        return context


class ExchangeRateHistory(ListView):

    context_object_name = 'exchange_rate_model'
    template_name = 'currency_history.html'
    context_object_name = 'exchange_rate_model'

    def get_context_data(self, **kwargs):
        context = super(ExchangeRateHistory, self).get_context_data(**kwargs)
        context['page_title'] = 'Exchange rate history'
        return context

    def get_queryset(self):
        print("hello")
        return ExchangeRate.objects.filter(currency__code=self.kwargs['code'])
