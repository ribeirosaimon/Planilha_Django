from rest_framework import generics
from rest_framework.response import Response
from .models import CarteiraModel
from .seralizers import CarteiraSerializers


class CarteiraView(generics.ListCreateAPIView):
    queryset = CarteiraModel.objects.all()
    serializer_class = CarteiraSerializers

    def list(self, request):
        queryset = self.queryset.filter(usuario = request.user)
        serializer = CarteiraSerializers(queryset, many=True)
        return Response(serializer.data)

    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user)


class ControlePatrimonioView(generics.ListAPIView):
    queryset = CarteiraModel.objects.all()
    serializer_class = CarteiraSerializers

    def list(self, request):
        acao = self.queryset.filter(usuario = request.user)
        #https://github.com/ribeirosaimon/controle_carteira/blob/main/core/classe_acao/acao_obj.py
        return Response()