from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import VendasViews


VendasRouter = SimpleRouter()
VendasRouter.register('venda', VendasViews)
