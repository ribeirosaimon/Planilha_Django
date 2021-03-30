from django import forms
from compras.models import CompraModel

class CompraModelForm(forms.ModelForm):
    class Meta:
        model = CompraModel
        fields = ['data', 'nacional','acao','quantidade','preco_medio'] 