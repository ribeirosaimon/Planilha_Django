from rest_framework import viewsets

from rest_framework.response import Response
from .serializers import PatrimonioSerializers
from .models import PatrimonioModel
from .relatorios.salvar_db import *


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
        queryset = self.queryset.filter(usuario = request.user)
        serializer = PatrimonioSerializers(queryset, many=True)
        return Response(serializer.data)