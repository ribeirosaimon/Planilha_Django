from django.urls import path
from .views import CarteiraView, ControlePatrimonioView

urlpatterns = [
    path('carteira/', CarteiraView.as_view(), name='carteira'),
    path('carteira/relatorio',ControlePatrimonioView.as_view(), name='carteira_relatorio')
]

