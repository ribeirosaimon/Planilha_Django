from .sraping_yahoo import *
from .get_dolar_price import *

def calc_lucro(acao, info_das_acoes):
    preco = 0
    ticket = list(acao.keys())[0]
<<<<<<< HEAD
    for x in info_das_acoes:
        if x['acao'] == ticket:
            preco = x['info'][0]['dados']['close']
    quantidade = acao[list((acao.keys()))[0]]['qtd']
    posicao = acao[list((acao.keys()))[0]]['pos']

    lucro = (preco * quantidade) - float(posicao)
    if acao[list((acao.keys()))[0]]['nacional'] == False:
        lucro *= get_dolar_price()
    return round(lucro, 2)


=======
    fechamento = float(info_das_acoes(ticket,nacional=acao[list(acao.keys())[0]]['nacional'])['info'][0]['dados']['close'])
    lucro = (fechamento * float(acao[ticket]['qtd'])) - float(acao[ticket]['pos'])
    return lucro
>>>>>>> 2f1ab6f197acba7c30f5cfda3683eecc66278bd8
