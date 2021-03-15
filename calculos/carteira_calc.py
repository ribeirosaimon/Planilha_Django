
def Sort(sub_li): 
    sub_li.sort(key = lambda x: x[0]) 
    return sub_li 

    
class Carteira:
    '''
    Portfolio stocks
    '''
    def __init__(self, CompraModel, VendaModel):
        self.CompraModel = CompraModel
        self.VendaModel = VendaModel
        self.carteira_atual()

        
    def carteira_atual(self):
        carteira = dict()
        organizar_carteira = []
        [organizar_carteira.append([x.data, x]) for x in self.CompraModel]
        [organizar_carteira.append([x.data, x]) for x in self.VendaModel]
        #percorrer as ações por ordem de data
        for acao in Sort(organizar_carteira):
            #se o model for uma compra
            if acao[1].__class__.__name__ == 'CompraModel':
                #se esse model ainda não tiver no dicionario
                if acao[1].acao not in carteira['compras']:
                    #adicionar o model no dicionario pra fazer a carteira
                    print('ok')
        