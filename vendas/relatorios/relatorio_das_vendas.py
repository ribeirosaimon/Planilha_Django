from calculos.carteira_calc import Carteira
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
        vendas_model = VendaModel.objects.filter(usuario=self.usuario)
        vendas_por_usuario = [x for x in vendas_model if x.data.month == self.mes and
            x.data.year == self.ano]
        self.calcular_lucro(vendas_por_usuario)


    def calcular_lucro(self, lista_vendas):
        lucro = 0
        for x in lista_vendas:
            posicao_na_compra = x.preco_venda * x.quantidade
            posicao_na_venda = x.preco_medio * x.quantidade
            retorno = posicao_na_venda - posicao_na_compra
