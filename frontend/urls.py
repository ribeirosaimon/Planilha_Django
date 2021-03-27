from django.urls import path, include
from django.views.generic.base import TemplateView

from .views import CarteiraView

urlpatterns = [
    path('',TemplateView.as_view(template_name='index.html'),name='index'),
    path('carteira/', CarteiraView.as_view(template_name='relatorio_carteira.html'), name='relatorio_carteira'),
    path('user/',include('django.contrib.auth.urls')),
]