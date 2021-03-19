from django.urls import path
from .views import CarteiraView, ControlePatrimonioView
from rest_framework.routers import SimpleRouter

CarteiraRouter = SimpleRouter()
CarteiraRouter.register('carteira', CarteiraView)
CarteiraRouter.register('relatorio/carteira',ControlePatrimonioView)
