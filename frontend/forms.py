from django import forms
from compras.models import CompraModel
from vendas.models import VendaModel



class CompraModelForm(forms.ModelForm):
    class Meta:
        model = CompraModel
        fields = ['data', 'nacional','acao','quantidade','preco_medio'] 


class VendaModelForm(forms.ModelForm):
    class Meta:
        model = VendaModel
        fields = ['data', 'nacional','acao','quantidade','preco_medio','preco_venda','dolar'] 
