from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import PatrimonioViews


PatrimonioRouter = SimpleRouter()
PatrimonioRouter.register('patrimonio', PatrimonioViews)
