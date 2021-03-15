from rest_framework import serializers
from .models import CompraModel

class CompraSerializers(serializers.ModelSerializer):
    class Meta:
        model = CompraModel
        fields = (
            'id',
            'data',
            'acao',
            'quantidade',
            'preco_medio',
        )
