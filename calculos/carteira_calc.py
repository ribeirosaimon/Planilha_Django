from .lucro import calc_lucro

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
        
    def minha_carteira(self):
        portfolio = self.carteira['compras']
        for x in range(len(portfolio)):
            acao = list(portfolio[x].keys())[0]
            portfolio[x][acao]['lucro'] = calc_lucro(portfolio[x])
        return portfolio
        
    def carteira_atual(self):
        compras = list()
        organizar_carteira = []
        [organizar_carteira.append([x.data, x]) for x in self.CompraModel]
        [organizar_carteira.append([x.data, x]) for x in self.VendaModel]
        #percorrer as ações por ordem de data
        for acao in Sort(organizar_carteira):   
            #se o model for uma compra
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
        for x in self.carteira['compras']:    
            if x[list(x.keys())[0]]['pos'] <= 0:
                self.carteira['compras'].remove(x)
        