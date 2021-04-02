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
                portfolio[x][acao]['preco_acao'] = self.preco_acao(acao)
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
                                x[acao[1].acao]['pm'] = round(x[acao[1].acao]['pos'] / x[acao[1].acao]['qtd'],2)
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
                    dict_patrimonio['acao']['posicao_usa'] += round(calculo_patrimonio(acao, x, self.precos_da_carteira),2)
                    
        dict_patrimonio['caixa']['caixa_total'] = round(dict_patrimonio['caixa']['caixa_br'] + (dict_patrimonio['caixa']['caixa_usa'] * get_dolar_price()),2)
        dict_patrimonio['acao']['posicao_total'] = round(dict_patrimonio['acao']['posicao_br'] + (dict_patrimonio['acao']['posicao_usa'] * get_dolar_price()),2)
        dict_patrimonio['valor_investido']['valor_total'] = round(dict_patrimonio['valor_investido']['valor_br'] +
            (dict_patrimonio['valor_investido']['valor_usa'] * get_dolar_price()),2)
        dict_patrimonio['patrimonio']['patrimonio_br'] = round(dict_patrimonio['acao']['posicao_br'] + dict_patrimonio['caixa']['caixa_br'],2)
        dict_patrimonio['patrimonio']['patrimonio_usa'] = round((dict_patrimonio['acao']['posicao_usa'] + dict_patrimonio['caixa']['caixa_usa']) * get_dolar_price(),2)
        dict_patrimonio['patrimonio']['patrimonio_total'] = round(dict_patrimonio['patrimonio']['patrimonio_usa'] + dict_patrimonio['patrimonio']['patrimonio_br'],2)
        return dict_patrimonio


    def relatorio_carteira(self):
        portfolio = self.carteira['compras']
        for x in range(len(portfolio)):
            acao = list(portfolio[x].keys())[0]
            if acao != 'caixa':
                portfolio[x][acao]['mma'] = self.media_movel_expodencial(acao)
                portfolio[x][acao]['topo_fundo'] = self.topo_fundo(acao)
                portfolio[x][acao]['hilo'] = self.indicador_hilo(acao)
                portfolio[x][acao]['bandas_de_bolinger'] = self.bandas_de_bolinger(acao)
                portfolio[x][acao]['rsi'] = self.rsi(acao)
                portfolio[x][acao]['avg_vol'] = self.avg_vol(acao)
                portfolio[x][acao]['preco_acao'] = self.preco_acao(acao)
                #Colocar preço da ação
        return portfolio
        

    
    #info de analises tecnicas



    def media_movel_expodencial(self, acao, tempo=20):
        fechamentos = []
        compra = False
        for valores in self.precos_da_carteira:
            if acao == valores['acao']:
                for index in range(0,tempo):
                    fechamento = valores['info'][index]['dados']['close']
                    fechamentos.append(fechamento)
        mma = round(sum(fechamentos) / tempo,2)
        close = fechamentos[0]
        if close < mma:
            compra = True
        dict_mma = {'mma':mma,
                    'info':{'buy':compra}}
        return dict_mma

    def topo_fundo(self, acao, tempo=2):
        contador_max, contador_min = 0,0
        resultado = [x['info'][0]['dados'] for x in self.precos_da_carteira if x['acao']== acao]
        candle_referencia = {'minima':resultado[0]['min'],'maxima':resultado[0]['max']}
        indicador = {'top':['none',0],'bottom':['none',0]}
        for valores in self.precos_da_carteira:
            if acao == valores['acao']:
                for dados in valores['info'][::-1]:
                    minimas = dados['dados']['min']
                    maximas = dados['dados']['max']
                    if maximas > candle_referencia['maxima']:
                        if contador_max < 2:
                            contador_max += 1
                        if contador_max >= 2:
                            contador_max += 1
                            contador_min = 0
                            candle_referencia['maxima'] = maximas
                            candle_referencia['minima'] = minimas
                            indicador['top'][0] = True
                            indicador['top'][1] = candle_referencia['maxima']
                            indicador['bottom'][0] = False

                    if minimas < candle_referencia['minima']:
                        if contador_min < 2:
                            contador_min += 1
                        if contador_min >= 2:
                            contador_min += 1
                            contador_max = 0
                            candle_referencia['maxima'] = maximas
                            candle_referencia['minima'] = minimas
                            indicador['top'][0] = False
                            indicador['bottom'][1] = candle_referencia['minima']
                            indicador['bottom'][0] = True
        return indicador

    
    def indicador_hilo(self,acao, candles=3):
        minimas, maximas =[], []
        fechamento = [x['info'][0]['dados']['close'] for x in self.precos_da_carteira if x['acao']== acao][0]
        for valores in self.precos_da_carteira:
            if acao == valores['acao']:
                for index in range(candles):
                    minima = valores['info'][index]['dados']['min']
                    maxima = valores['info'][index]['dados']['max']
                    minimas.append(minima)
                    maximas.append(maxima)

        mma_minima = round(sum(minimas) / 3,2)
        mma_maxima = round(sum(maximas)/3,2)
        dict_hilo = {'hilo':'none',
                     'info':{'top':mma_maxima,'bottom':mma_minima}}
        if fechamento < mma_minima:
            dict_hilo['hilo'] = 'buy'
        if fechamento > mma_maxima:
            dict_hilo['hilo'] = 'sell'
        return dict_hilo


    def bandas_de_bolinger(self,acao,tempo=20):
        fechamentos,lista_quadrados = [],[]
        dict_bolinger = {'bollinger':'none',
                         'dados':{'top':0,
                                  'bottom':0}}
        fechamento = [x['info'][0]['dados']['close'] for x in self.precos_da_carteira if x['acao']== acao][0] 
        for valores in self.precos_da_carteira:
            if acao == valores['acao']:
                for index in range(0,tempo):
                    fechamento = valores['info'][index]['dados']['close']
                    fechamentos.append(fechamento)
        mma = sum(fechamentos) / tempo
        for x in range(tempo):
            calculo = (mma - fechamentos[x]) ** 2
            lista_quadrados.append(calculo)
        desvio_padrao = (sum(lista_quadrados) / tempo) **0.5
        banda_superior = round(mma + (desvio_padrao * 2),2)
        banda_inferior = round(mma - (desvio_padrao * 2),2)
        if fechamento < banda_inferior:
            dict_bolinger['bollinger'] = 'buy'
        if fechamento > banda_superior:
            dict_bolinger['bollinger'] = 'sell'
        dict_bolinger['dados']['top'] = banda_superior
        dict_bolinger['dados']['bottom'] = banda_inferior
        return dict_bolinger

        #rsi
    def rsi(self,acao, tempo=14, min_ifr=30, max_ifr=70):
        media_ganho, media_perda = [],[]
        for valores in self.precos_da_carteira:
            if acao == valores['acao']:
                for index in range(0,tempo):
                    fechamento = valores['info'][index]['dados']['close']
                    abertura = valores['info'][index]['dados']['open']
                    calculo = abs(fechamento - abertura)
                    if fechamento > abertura:
                        media_ganho.append(calculo)
                    if fechamento < abertura:
                        media_perda.append(calculo)
        fr = (sum(media_ganho) / tempo) / (sum(media_perda) / tempo)
        ifr = round(100 - (100/(1+fr)),2)
        dict_ifr = {'ifr':ifr,'dados':'none'}
        if ifr < min_ifr:
            dict_ifr['dados'] = 'buy'
        if ifr > max_ifr:
            dict_ifr['dados'] = 'sell'
        return dict_ifr

    def avg_vol(self,acao):
        avg_vol = []
        volume_diario = [x['info'][0]['dados']['volume'] for x in self.precos_da_carteira if x['acao']== acao][0]
        for valores in self.precos_da_carteira:
            if acao == valores['acao']:
                for dados in valores['info']:
                    volume = dados['dados']['volume']
                    avg_vol.append(volume)
        volume_medio = int(round(sum(avg_vol)/len(avg_vol),0))
        return calculo_de_volume(volume_medio,volume_diario)

    def preco_acao(self,acao):
        for valores in self.precos_da_carteira:
            if acao == valores['acao']:
                return valores['info'][0]['dados']['close']