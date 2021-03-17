from .sraping_yahoo import *


def calc_lucro(acao):
    ticket = list(acao.keys())[0]
    fechamento = float(info_das_acoes(ticket,nacional=acao[list(acao.keys())[0]]['nacional'])['info'][0]['dados']['close'])
    lucro = (fechamento * float(acao[ticket]['qtd'])) - float(acao[ticket]['pos'])
    return lucro
