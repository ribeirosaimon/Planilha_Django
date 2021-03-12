from rest_framework import generics
from rest_framework.response import Response
from .models import CarteiraModel
from .seralizers import CarteiraSerializers


class CarteiraView(generics.ListCreateAPIView):
    queryset = CarteiraModel.objects.all()
    serializer_class = CarteiraSerializers
    def list(self, request):
        # Note the use of `get_queryset()` instead of `self.queryset`
        queryset = self.get_queryset(usuario = request.user)
        serializer = CarteiraSerializers(queryset, many=True)
        return Response(serializer.data)