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