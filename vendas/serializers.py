from rest_framework import serializers
from .models import VendaModel

class VendaSerializers(serializers.ModelSerializer):
    class Meta:
        model = VendaModel
        fields = (
            'id',
            'nacional',
            'data',
            'acao',
            'quantidade',
            'preco_medio',
            'preco_venda',
            'dolar'
        )
