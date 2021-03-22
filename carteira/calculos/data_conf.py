from datetime import datetime, timedelta, date
import requests

def data_utc(data_str, mes_passado = False):
    data = datetime.strptime(data_str, '%Y-%m-%d').date()
    data = data - timedelta(hours=-3)
    if mes_passado == True:
        data = data - timedelta(days=92)
    data = data - datetime(1970, 1, 1).date()
    return int(data.total_seconds())

def data_de_hoje(data_str=True,delta=0):
    hora_do_dia = int(datetime.now().strftime('%H'))
    data = date.today()
    if delta == 0:
        if hora_do_dia < 9:
            data = data - timedelta(days=1)
        if data_str == True:
            return str(data)
        else:
            return data
    if delta > 0:
        if hora_do_dia < 9:
            tempo = 1 + delta
            data = data - timedelta(days=tempo)
        if data_str == True:
            return str(data - timedelta(days=delta))
        else:
            return data - timedelta(days=delta)


def data_iso(data_str):
    UTC_datetime_converted = datetime.utcfromtimestamp(data_str).date().strftime("%Y-%m-%d")
    return UTC_datetime_converted


def get_dolar_price():
    endpoint  = 'https://economia.awesomeapi.com.br/json/daily/USD-BRL/2'
    resposta = requests.request('GET', endpoint)
    dolar_do_dia =  float(resposta.json()[0]['ask'])
    #dolar_ultimo_dia = float(resposta.json()[1]['ask'])
    return dolar_do_dia
