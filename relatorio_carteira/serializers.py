from rest_framework import serializers
from .models import PatrimonioModel

class PatrimonioSerializers(serializers.ModelSerializer):
    class Meta:
        model = PatrimonioModel
        fields = (
            'id',
            'data',
            'patrimonio_total',
            'patrimonio_br',
            'patrimonio_usa',
            'vol_total',
            'vol_br',
            'vol_usa'
        )
