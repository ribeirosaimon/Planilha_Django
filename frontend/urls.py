from django.urls import path, include
from django.views.generic.base import TemplateView

from .views import CarteiraView, AnaliseTecnicaView

urlpatterns = [
    path('',TemplateView.as_view(template_name='index.html'),name='index'),
    path('carteira/', CarteiraView.as_view(template_name='relatorio_carteira.html'), name='relatorio_carteira'),
    path('analise_tecnica/', AnaliseTecnicaView.as_view(template_name='analise_tecnica.html'), name='analise_tecnica'),
    path('user/',include('django.contrib.auth.urls')),
]