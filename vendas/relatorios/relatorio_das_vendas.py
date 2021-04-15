from carteira.calculos.carteira_calc import Carteira
from vendas.models import VendaModel
from datetime import datetime

class RelatorioVendas():

    def __init__(self, mes, ano, usuario):
        try:
            self.mes = int(mes)
        except:
            self.mes = datetime.today().month
        try:
            self.ano = int(ano)
        except:
            self.ano = datetime.today().year
        self.usuario = usuario
        self.imposto_de_renda()


    def imposto_de_renda(self):
        dict_imposto_de_renda = {
            'imposto_de_renda': {
                'lucro_mensal':'',
                'mov_mensal':'',
                'pagamento':'',
            }
        }
        vendas_model = VendaModel.objects.filter(usuario=self.usuario)
        vendas_por_usuario = [x for x in vendas_model if x.data.month == self.mes and
            x.data.year == self.ano]
        dict_imposto_de_renda['imposto_de_renda']['lucro_mensal'] = self.calcular_lucro(vendas_por_usuario)
        dict_imposto_de_renda['imposto_de_renda']['mov_mensal'] = self.movimentacao_mensal(vendas_por_usuario)
        dict_imposto_de_renda['imposto_de_renda']['pagamento'] = self.pagamento_de_imposto(dict_imposto_de_renda['imposto_de_renda']['mov_mensal'], dict_imposto_de_renda['imposto_de_renda']['lucro_mensal'])
        return dict_imposto_de_renda
    

    def calcular_lucro(self, lista_vendas):
        lucro_br, lucro_usa, lucro_total = 0,0,0 
        for x in lista_vendas:
            posicao_na_venda = x.preco_venda * x.quantidade
            posicao_na_compra = x.preco_medio * x.quantidade
            retorno = posicao_na_venda - posicao_na_compra
            if x.nacional == True:
                lucro_br += retorno
            if x.nacional == False:
                retorno = retorno * x.dolar
                lucro_usa += retorno
            lucro_total += retorno
        dict_retorno = {
            'lucro': {
                'lucro_total':round(lucro_total,2),
                'lucro_br':round(lucro_br,2),
                'lucro_usa':round(lucro_usa,2),
            }
        }
        return dict_retorno

    def pagamento_de_imposto(self, dict_mov, lucro):
        dict_pagamento = {
            'darf':{
                'darf_br':0,
                'darf_usa':0,
            }
        }
        if dict_mov['movimentacao']['mov_br'] > 20000:
            ir_devido = float(lucro['lucro']['lucro_br']) * 0.15
            dict_pagamento['darf']['darf_br'] = round(ir_devido,2)
        if dict_mov['movimentacao']['mov_usa'] > 35000:
            ir_devido = float(lucro['lucro']['lucro_usa']) * 0.15
            dict_pagamento['darf']['darf_usa'] = round(ir_devido,2)
        return dict_pagamento


    def movimentacao_mensal(self, lista_vendas):
        dict_mov = {
            'movimentacao':{
                'mov_br':0,
                'mov_usa':0
            },
            'isencao_mov':{
                'isento_br':0,
                'isento_usa':0
            }
        }
        for x in lista_vendas:
            movimentacao = x.preco_venda * x.quantidade
            if x.nacional == True:
                dict_mov['movimentacao']['mov_br'] += round(movimentacao,2)
            if x.nacional == False:
                movimentacao *= x.dolar
                dict_mov['movimentacao']['mov_usa'] += round(movimentacao,2)
        dict_mov['isencao_mov']['isento_br'] = round(19999.99 - float(dict_mov['movimentacao']['mov_br']),2)
        dict_mov['isencao_mov']['isento_usa'] = round(34999.99 - float(dict_mov['movimentacao']['mov_usa']),2)
        if dict_mov['isencao_mov']['isento_br'] < 0:
            dict_mov['isencao_mov']['isento_br'] = 0
        if dict_mov['isencao_mov']['isento_usa'] < 0:
            dict_mov['isencao_mov']['isento_usa'] = 0
        return dict_mov

    def relatorio_de_vendas(self):
        dict_mensal = dict()
        vendas_model = VendaModel.objects.filter(usuario=self.usuario)

        for _ in range(1,13):
            vendas_model = VendaModel.objects.filter(usuario=self.usuario)
            vendas_por_usuario = [x for x in vendas_model if x.data.month == _ and
                x.data.year == self.ano]
            dict_mov_mensal = self.movimentacao_mensal(vendas_por_usuario)
            darf = self.pagamento_de_imposto(dict_mov_mensal, self.calcular_lucro(vendas_por_usuario))
            dict_mensal[_] = darf
        return dict_mensal


