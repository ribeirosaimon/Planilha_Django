from rest_framework import viewsets
from rest_framework.response import Response
from compras.models import CompraModel
from vendas.models import VendaModel
from compras.serializers import CompraSerializers
from calculos.carteira_calc import Carteira



class CarteiraView(viewsets.ViewSet):
    queryset = CompraModel.objects.all()
    serializer_class = CompraSerializers
    def list(self, request):
        compra_model_user = CompraModel.objects.filter(usuario=request.user)
        venda_model_user = VendaModel.objects.filter(usuario=request.user)
        carteira = Carteira(compra_model_user, venda_model_user)
        meu_portfolio = carteira.minha_carteira()
        return Response({'carteira':meu_portfolio})

class ControlePatrimonioView(viewsets.ViewSet):
    queryset = CompraModel.objects.all()
    serializer_class = CompraSerializers

    def list(self, request):
        acao = self.queryset.filter(usuario = request.user)
        return Response({'acao':f'{acao}'})
