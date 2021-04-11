from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import PatrimonioViews, RelatorioPatrimonioViews


PatrimonioRouter = SimpleRouter()
PatrimonioRouter.register('patrimonio', PatrimonioViews)
PatrimonioRouter.register('relatorio/patrimonio', RelatorioPatrimonioViews)