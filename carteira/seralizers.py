from rest_framework import serializers
from .models import CarteiraModel

class CarteiraSerializers(serializers.ModelSerializer):
    class Meta:
        model = CarteiraModel
        fields = (
            'id',
            'acao',
            'quantidade',
            'preco_medio',
        )