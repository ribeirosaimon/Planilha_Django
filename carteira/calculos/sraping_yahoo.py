from datetime import datetime, timedelta, date
from .data_conf import *
import requests


def info_das_acoes(acao, nacional=True):
    informacao_retorno = []
    data = str(date.today())
    url_acao = acao
    if nacional == True:
        url_acao = f'{acao}.sa'
    url = f'https://query2.finance.yahoo.com/v8/finance/chart/{url_acao}?symbol={url_acao}&period1={data_utc(data, mes_passado=True)}&period2={data_utc(data, mes_passado=False)}&interval=1d&includePrePost=true&events=div%2Csplit'
    info = requests.get(url)
    fechamento = info.json()['chart']['result'][0]['indicators']['quote'][0]['close']
    abertura = info.json()['chart']['result'][0]['indicators']['quote'][0]['open']
    minima = info.json()['chart']['result'][0]['indicators']['quote'][0]['low']
    maxima = info.json()['chart']['result'][0]['indicators']['quote'][0]['high']
    volume = info.json()['chart']['result'][0]['indicators']['quote'][0]['volume']
    data = info.json()['chart']['result'][0]['timestamp']
    for index in range(len(fechamento)):
        try:
            dicionario = {
                            'data':data_iso(data[index]),
                            'dados':
                                {
                                    'close':round(fechamento[index],2),
                                    'open':round(abertura[index],2),
                                    'min':round(minima[index],2),
                                    'max':round(maxima[index],2),
                                    'volume':round(volume[index],2),
                                }
                        }            
            informacao_retorno.append(dicionario)
        except:
            pass
    informacao_retorno = informacao_retorno[::-1]
    dict_info = {
                'acao':acao,
                'info':informacao_retorno}
    return dict_info