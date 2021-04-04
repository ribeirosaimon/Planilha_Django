import requests
from django.conf import settings

def get_dolar_price():
    return settings.DOLAR_TODAY

def preco_dolar():
    endpoint  = 'https://economia.awesomeapi.com.br/json/daily/USD-BRL/2'
    resposta = requests.request('GET', endpoint)
    dolar_do_dia =  float(resposta.json()[0]['ask'])
    return dolar_do_dia
