from .sraping_yahoo import *
from .get_dolar_price import *

def calc_lucro(acao, info_das_acoes):
    preco = 0
    ticket = list(acao.keys())[0]
    for x in info_das_acoes:
        if x['acao'] == ticket:
            preco = x['info'][0]['dados']['close']
    quantidade = acao[list((acao.keys()))[0]]['qtd']
    posicao = acao[list((acao.keys()))[0]]['pos']
    lucro = (preco * quantidade) - float(posicao)
    if acao[list((acao.keys()))[0]]['nacional'] == False:
        lucro *= get_dolar_price()
    return round(lucro, 2)

def calculo_patrimonio(acao, lista_info, precos_da_carteira):
    patrimonio = 0
    for y in precos_da_carteira:
        if y['acao'] == acao:
            preco = y['info'][0]['dados']['close']
            patrimonio += lista_info[acao]['qtd'] * preco
    return round(patrimonio,2)


def calculo_de_volume(volume_medio,volume_diario,horario_comercial=8,inicio_expediente=10):
    hora_do_dia = int(datetime.now().strftime('%H'))
    minuto_do_dia = int(datetime.now().strftime('%M'))
    if minuto_do_dia > 45:
        hora_do_dia = hora_do_dia + 1
    tempo_de_expediente = hora_do_dia - inicio_expediente
    if 0 > tempo_de_expediente or tempo_de_expediente > 8:
        tempo_de_expediente = 8
    volume_medio_por_hora = int(round(volume_medio / horario_comercial,0))
    volume_medio_do_dia = volume_medio_por_hora * tempo_de_expediente
    if volume_diario != 0:
        porcentagem_diferenca = round((volume_medio_do_dia/ volume_diario)-1,2)
    else:
        porcentagem_diferenca = 0
    dict_volume = {'volume':volume_diario,
                    'dados':{'avg_vol':volume_medio,
                             'high':'none',
                             'percent':porcentagem_diferenca}}

    if volume_diario > volume_medio_do_dia:
        dict_volume['dados']['high'] = True
    else:
        dict_volume['dados']['high'] = False
    return dict_volume