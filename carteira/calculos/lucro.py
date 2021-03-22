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