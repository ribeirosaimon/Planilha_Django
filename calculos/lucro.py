from .sraping_yahoo import *


def calc_lucro(acao):
    ticket = list(acao.keys())[0]
    x = info_das_acoes(ticket,nacional=acao[list(acao.keys())[0]]['nacional'])
    print(x['info'])
    return 'ok'
