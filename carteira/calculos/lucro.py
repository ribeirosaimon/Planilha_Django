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


def calculo_de_volume(volume_medio,volume_diario,horario_comercial=7,inicio_expediente=10):
    hora_do_dia = int(datetime.now().strftime('%H'))
    minuto_do_dia = int(datetime.now().strftime('%M'))
    if minuto_do_dia > 45:
        hora_do_dia = hora_do_dia + 1
    tempo_de_expediente = hora_do_dia - inicio_expediente
    if 0 > tempo_de_expediente or tempo_de_expediente > horario_comercial:
        tempo_de_expediente = horario_comercial
    #se o dia for sabado ou domingo
    dia_de_hoje = datetime.today().weekday()
    if dia_de_hoje >= 5:
        tempo_de_expediente = horario_comercial
    volume_medio_por_hora = int(round(volume_medio / horario_comercial,0))
    volume_medio_do_dia = volume_medio_por_hora * tempo_de_expediente
    if volume_diario != 0:
        porcentagem_diferenca = round(((volume_diario / volume_medio_do_dia)-1) * 100,1)
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

def correcao_carteira_com_peso(portfolio, patrimonio):
    patrimonio_total = patrimonio['patrimonio']['patrimonio_total']['pos']
    lista_retorno = []
    for x in portfolio:
        acao = list(x.keys())[0]
        if acao == 'caixa':
            posicao = round((float(x[acao]['pos']) / patrimonio_total * 100),1)
            x[acao]['peso'] = posicao
        if acao != 'caixa':
            if x[acao]['nacional'] == True:
                posicao = round((float(x[acao]['posicao_atual']) / patrimonio_total * 100),1)
                retorno_total = round((float(x[acao]['lucro']) /  patrimonio_total) * 100,1)                
                x[acao]['peso'] = posicao
                x[acao]['retorno_no_patrimonio'] = retorno_total
            else:
                posicao = round(((float(x[acao]['posicao_atual']) * get_dolar_price()) / patrimonio_total * 100),1)
                retorno_total = round((float(x[acao]['lucro']) / patrimonio_total * 100),1)
                x[acao]['peso'] = posicao
                x[acao]['retorno_no_patrimonio'] = retorno_total
        lista_retorno.append(x)
    return lista_retorno
