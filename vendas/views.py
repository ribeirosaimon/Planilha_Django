from rest_framework import viewsets

from rest_framework.response import Response
from .serializers import VendaSerializers
from .models import VendaModel

class VendasViews(viewsets.ModelViewSet):
    queryset = VendaModel.objects.all()
    serializer_class = VendaSerializers
    def list(self, request):
        queryset = self.queryset.filter(usuario = request.user)
        serializer = VendaSerializers(queryset, many=True)
        return Response(serializer.data)

    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user)


