from django.contrib import admin
from .models import CompraModel

@admin.register(CompraModel)
class CompraAdmin(admin.ModelAdmin):
    list_display = ('acao','quantidade', 'preco_medio')
