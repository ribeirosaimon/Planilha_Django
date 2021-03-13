from django.contrib import admin
from .models import VendaModel

@admin.register(VendaModel)
class CompraAdmin(admin.ModelAdmin):
    list_display = ('acao','quantidade', 'preco_medio')
