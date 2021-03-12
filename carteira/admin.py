from django.contrib import admin
from .models import CarteiraModel

@admin.register(CarteiraModel)
class CarteiraAdmin(admin.ModelAdmin):
    list_display = ('acao','quantidade', 'preco_medio')
