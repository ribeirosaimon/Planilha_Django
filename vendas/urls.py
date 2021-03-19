from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import VendasViews, RelatorioVendasViews


VendasRouter = SimpleRouter()
VendasRouter.register('venda', VendasViews)
VendasRouter.register('relatorio/venda', RelatorioVendasViews)
