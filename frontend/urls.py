from django.urls import path, include
from django.views.generic.base import TemplateView

from .views import CarteiraView, AnaliseTecnicaView, RelatorioImpostoRenda

urlpatterns = [
    path('',TemplateView.as_view(template_name='index.html'),name='index'),
    path('carteira/', CarteiraView.as_view(template_name='relatorio_carteira.html'), name='relatorio_carteira'),
    path('analise_tecnica/', AnaliseTecnicaView.as_view(template_name='analise_tecnica.html'), name='analise_tecnica'),
    path('relatorio_ir/', RelatorioImpostoRenda.as_view(template_name='relatorio_ir.html'), name='relatorio_ir'),
    path('user/',include('django.contrib.auth.urls')),
]