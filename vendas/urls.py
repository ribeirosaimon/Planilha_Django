from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import VendaViews


VendasRouter = SimpleRouter()
VendasRouter.register('venda', VendaViews)
