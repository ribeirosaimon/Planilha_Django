from rest_framework import viewsets

from rest_framework.response import Response
from .serializers import PatrimonioSerializers

from compras.models import CompraModel
from vendas.models import VendaModel
from .models import PatrimonioModel

from .relatorios.salvar_db import *
from carteira.calculos.carteira_calc import Carteira

class PatrimonioViews(viewsets.ViewSet):
    queryset = PatrimonioModel.objects.all()
    serializer_class = PatrimonioSerializers

    def list(self, request):
        queryset = self.queryset.filter(usuario = request.user)
        serializer = PatrimonioSerializers(queryset, many=True)
        return Response(serializer.data)

    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user)



class RelatorioPatrimonioViews(viewsets.ViewSet):
    queryset = PatrimonioModel.objects.all()
    serializer_class = PatrimonioSerializers

    def list(self, request):
        compra_model_user = CompraModel.objects.filter(usuario=request.user)
        venda_model_user = VendaModel.objects.filter(usuario=request.user)
        carteira = Carteira(compra_model_user, venda_model_user)
        volatilidade_implicita = carteira.vol_implicita()
        return Response({
            'volatilidade': volatilidade_implicita
            })
