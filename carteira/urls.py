from django.urls import path
from .views import CarteiraView

urlpatterns = [
    path('carteira/', CarteiraView.as_view(), name='carteira'),
]

