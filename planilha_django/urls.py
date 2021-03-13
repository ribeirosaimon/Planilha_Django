from django.contrib import admin
from django.urls import path, include
from compras.urls import ComprasRouter
from carteira.urls import CarteiraRouter
from vendas.urls import VendasRouter

urlpatterns = [
    path('api/v1/', include(CarteiraRouter.urls)),
    path('api/v1/', include(ComprasRouter.urls)),
    path('api/vi/', include(VendasRouter.urls)),
    path('admin/', admin.site.urls),
    path('auth/', include('rest_framework.urls'))
]


