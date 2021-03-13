from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import CompraViews


ComprasRouter = SimpleRouter()
ComprasRouter.register('compra', CompraViews)
