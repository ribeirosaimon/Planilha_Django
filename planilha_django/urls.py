from django.contrib import admin
from django.urls import path, include
from carteira.urls import CarteiraRouter
from compras.urls import ComprasRouter
from vendas.urls import VendasRouter

urlpatterns = [
    path('api/v1/', include(ComprasRouter.urls)),
    path('api/v1/', include(VendasRouter.urls)),
    path('api/v1/', include(CarteiraRouter.urls)),
    
    path('admin/', admin.site.urls),
    path('auth/', include('rest_framework.urls'))
]


