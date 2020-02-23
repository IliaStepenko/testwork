from django.urls import path

from . import views

urlpatterns = [

    path('', views.ActualExchangeRate.as_view(), name='index'),
    path('currencylist/<slug:code>', views.ExchangeRateHistory.as_view())

]