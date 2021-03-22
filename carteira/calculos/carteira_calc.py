from .lucro import calc_lucro
from .sraping_yahoo import *
from .get_dolar_price import *
from .lucro import *

def Sort(sub_li): 
    sub_li.sort(key = lambda x: x[0]) 
    return sub_li 

    
class Carteira:
    '''
    Portfolio stocks
    '''
    def __init__(self, CompraModel, VendaModel):
        self.carteira = {
            'compras':[]
            }
        self.CompraModel = CompraModel
        self.VendaModel = VendaModel
        self.carteira_atual()

        #nome das ações e nacional
        self.precos_da_carteira = [
            info_das_acoes(list(self.carteira['compras'][x].keys())[0],
            list(self.carteira['compras'][x].values())[0]['nacional'])
            for x in range(len(self.carteira['compras'])) if list(self.carteira['compras'][x].keys())[0] != 'caixa']
        
    def minha_carteira(self):
        portfolio = self.carteira['compras']
        for x in range(len(portfolio)):
            acao = list(portfolio[x].keys())[0]
            if acao != 'caixa':
                portfolio[x][acao]['lucro'] = calc_lucro(portfolio[x], self.precos_da_carteira)
        return portfolio
        
    def carteira_atual(self):
        compras = list()
        organizar_carteira = []
        [organizar_carteira.append([x.data, x]) for x in self.CompraModel]
        [organizar_carteira.append([x.data, x]) for x in self.VendaModel]
        #percorrer as ações por ordem de data
        for acao in Sort(organizar_carteira):   
            #se o model for uma compra
            if acao[1].acao == 'caixa':
                dict_caixa = {
                            'caixa':
                                {
                                    'nacional':acao[1].nacional,
                                    'pm':acao[1].preco_medio,
                                    'qtd':acao[1].quantidade,
                                    'pos':acao[1].preco_medio * acao[1].quantidade
                                }
                        }
                if acao[1].nacional == False:
                    dict_caixa['caixa']['pos'] = round(float(dict_caixa['caixa']['pos']) * get_dolar_price(),2)

                compras.append(dict_caixa)
            else:
                if acao[1].__class__.__name__ == 'CompraModel':
                    #se esse model ainda não tiver no dicionario
                    if acao[1].acao not in [list(x.keys())[0] for x in compras]:
                        #adicionar o model no dicionario pra fazer a carteira
                        dict_acao = {
                            acao[1].acao:
                                {
                                    'nacional':acao[1].nacional,
                                    'pm':acao[1].preco_medio,
                                    'qtd':acao[1].quantidade,
                                    'pos':acao[1].preco_medio * acao[1].quantidade
                                }
                        }
                        compras.append(dict_acao)
                    else:
                        for x in compras:
                            if list(x.keys())[0] == acao[1].acao:
                                pos = acao[1].preco_medio * acao[1].quantidade
                                x[acao[1].acao]['qtd'] += acao[1].quantidade
                                x[acao[1].acao]['pos'] += pos
                                x[acao[1].acao]['pm'] = x[acao[1].acao]['pos'] / x[acao[1].acao]['qtd']
                    self.carteira['compras'] = compras
                if acao[1].__class__.__name__ == 'VendaModel':
                    if acao[1].acao in [list(x.keys())[0] for x in self.carteira['compras']]:
                        for x in self.carteira['compras']:
                            if list(x.keys())[0] == acao[1].acao:
                                pos = acao[1].preco_medio * acao[1].quantidade
                                x[acao[1].acao]['pos'] -= pos
                                x[acao[1].acao]['qtd']-= acao[1].quantidade
            for x in self.carteira['compras']:    
                if x[list(x.keys())[0]]['pos'] <= 0:
                    self.carteira['compras'].remove(x)
        
    def patrimonio(self, dicionario):
        dict_patrimonio = {
            'patrimonio':{
                'patrimonio_total':0,
                'patrimonio_br':0,
                'patrimonio_usa':0
            },
            'caixa': {
                'caixa_total':0,
                'caixa_br':0,
                'caixa_usa':0
            },
            'acao': {
                'posicao_total':0,
                'posicao_br':0,
                'posicao_usa':0
            },
            'valor_investido': {
                'valor_total':0,
                'valor_br':0,
                'valor_usa':0
            }
        }
        for x in dicionario:
            acao = list(x.keys())[0]
            if acao == 'caixa':
                if x['caixa']['nacional'] == True:
                    dict_patrimonio['caixa']['caixa_br'] += round(float(x['caixa']['pm']),2)
                if x['caixa']['nacional'] == False:
                    dict_patrimonio['caixa']['caixa_usa'] += round(float(x['caixa']['pm']),2)
            else:
                if x[acao]['nacional'] == True:
                    dict_patrimonio['valor_investido']['valor_br'] += round(float(x[acao]['pos']),2)
                    dict_patrimonio['acao']['posicao_br'] += calculo_patrimonio(acao, x, self.precos_da_carteira)
                if x[acao]['nacional'] == False:
                    dict_patrimonio['valor_investido']['valor_usa'] += round(float(x[acao]['pos']),2)
                    dict_patrimonio['acao']['posicao_usa'] += calculo_patrimonio(acao, x, self.precos_da_carteira)
                    
        dict_patrimonio['caixa']['caixa_total'] = round(dict_patrimonio['caixa']['caixa_br'] + (dict_patrimonio['caixa']['caixa_usa'] * get_dolar_price()),2)
        dict_patrimonio['acao']['posicao_total'] = round(dict_patrimonio['acao']['posicao_br'] + (dict_patrimonio['acao']['posicao_usa'] * get_dolar_price()),2)
        dict_patrimonio['valor_investido']['valor_total'] = round(dict_patrimonio['valor_investido']['valor_br'] +
            (dict_patrimonio['valor_investido']['valor_usa'] * get_dolar_price()),2)
        dict_patrimonio['patrimonio']['patrimonio_br'] = round(dict_patrimonio['acao']['posicao_br'] + dict_patrimonio['caixa']['caixa_br'],2)
        dict_patrimonio['patrimonio']['patrimonio_usa'] = round((dict_patrimonio['acao']['posicao_usa'] * get_dolar_price()) + dict_patrimonio['caixa']['caixa_usa'],2)
        dict_patrimonio['patrimonio']['patrimonio_total'] = round(dict_patrimonio['patrimonio']['patrimonio_usa'] + dict_patrimonio['patrimonio']['patrimonio_br'],2)
        return dict_patrimonio


    def relatorio_carteira(self):
        portfolio = self.carteira['compras']
        for x in range(len(portfolio)):
            acao = list(portfolio[x].keys())[0]
            portfolio[x][acao]['lucro'] = 100000000000000
        return portfolio
        
