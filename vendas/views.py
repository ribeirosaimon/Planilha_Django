from rest_framework import viewsets

from rest_framework.response import Response
from .serializers import VendaSerializers
from .models import VendaModel

class VendaViews(viewsets.ModelViewSet):
    queryset = VendaModel.objects.all()
    serializer_class = VendaSerializers 
    def list(self, request):
        return Response({'venda':'ok'})