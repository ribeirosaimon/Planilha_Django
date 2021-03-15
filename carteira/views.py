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
        return Response({'acao':'ok'})

class ControlePatrimonioView(viewsets.ViewSet):
    queryset = CompraModel.objects.all()
    serializer_class = CompraSerializers

    def list(self, request):
        acao = self.queryset.filter(usuario = request.user)
        #https://github.com/ribeirosaimon/controle_carteira/blob/main/core/classe_acao/acao_obj.py
        return Response({'acao':f'{acao}'})
