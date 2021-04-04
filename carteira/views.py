from rest_framework import viewsets
from rest_framework.response import Response
from compras.models import CompraModel
from vendas.models import VendaModel
from compras.serializers import CompraSerializers
from .calculos.carteira_calc import Carteira
from .calculos.lucro import correcao_carteira_com_peso


class CarteiraView(viewsets.ViewSet):
    queryset = CompraModel.objects.all()
    serializer_class = CompraSerializers
    def list(self, request):
        compra_model_user = CompraModel.objects.filter(usuario=request.user)
        venda_model_user = VendaModel.objects.filter(usuario=request.user)
        carteira = Carteira(compra_model_user, venda_model_user)
        meu_portfolio = carteira.minha_carteira()
        patrimonio = carteira.patrimonio()
        portfolio_atualizado = correcao_carteira_com_peso(meu_portfolio, patrimonio)
        return Response({
            'patrimonio':patrimonio,
            'carteira':portfolio_atualizado
            })


class ControlePatrimonioView(viewsets.ViewSet):
    queryset = CompraModel.objects.all()
    serializer_class = CompraSerializers
    def list(self, request):
        compra_model_user = CompraModel.objects.filter(usuario=request.user)
        venda_model_user = VendaModel.objects.filter(usuario=request.user)
        carteira = Carteira(compra_model_user, venda_model_user)
        meu_portfolio = carteira.relatorio_carteira()
        return Response({'carteira':meu_portfolio})