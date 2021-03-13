from rest_framework import viewsets

from rest_framework.response import Response
from .serializers import CompraSerializers
from .models import CompraModel

class CompraViews(viewsets.ModelViewSet):
    queryset = CompraModel.objects.all()
    serializer_class = CompraSerializers

    def list(self, request):
        queryset = self.queryset.filter(usuario = request.user)
        serializer = CompraSerializers(queryset, many=True)
        return Response(serializer.data)

    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user)


