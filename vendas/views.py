from rest_framework import viewsets

from rest_framework.response import Response
from .serializers import VendaSerializers
from .models import VendaModel
from .relatorios.relatorio_das_vendas import RelatorioVendas

class VendasViews(viewsets.ModelViewSet):
    queryset = VendaModel.objects.all()
    serializer_class = VendaSerializers
    def list(self, request):
        queryset = self.queryset.filter(usuario = request.user)
        serializer = VendaSerializers(queryset, many=True)
        return Response(serializer.data)

    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user)


class RelatorioVendasViews(viewsets.ViewSet):
    queryset = VendaModel.objects.all()
    serializer_class = VendaSerializers
    def list(self, request):
        ano_info = self.request.query_params.get('ano')
        mes_info = self.request.query_params.get('mes')
        vendas = RelatorioVendas(mes_info, ano_info,request.user)
        
        return Response({
            'relatorio':vendas.imposto_de_renda(),
            'vendas_anuais':vendas.relatorio_de_vendas(),
            })