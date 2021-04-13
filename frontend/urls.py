from django.urls import path, include
from django.views.generic.base import TemplateView

from .views import CarteiraView, AnaliseTecnicaView, RelatorioImpostoRenda, CompraFormView, VendaFormView, CaixaBRFormView, CaixaUSAFormView, PatrimonioView

urlpatterns = [
    path('',TemplateView.as_view(template_name='index.html'),name='index'),
    path('carteira/', CarteiraView.as_view(template_name='relatorio_carteira.html'), name='relatorio_carteira'),
    path('analise_tecnica/', AnaliseTecnicaView.as_view(template_name='analise_tecnica.html'), name='analise_tecnica'),
    path('relatorio_ir/', RelatorioImpostoRenda.as_view(template_name='relatorio_ir.html'), name='relatorio_ir'),
    path('compra/', CompraFormView.as_view(template_name='compra_form.html'), name='compra_form'),
    path('venda/', VendaFormView.as_view(template_name='venda_form.html'), name='venda_form'),
    path('caixabr/', CaixaBRFormView.as_view(template_name='caixa_form.html'), name='caixa_form_br'),
    path('caixausa/', CaixaUSAFormView.as_view(template_name='caixa_form.html'), name='caixa_form_usa'),
    path('patrimonio/', PatrimonioView.as_view(template_name='patrimonio.html'), name='patrimonio'),
    path('user/',include('django.contrib.auth.urls')),
]