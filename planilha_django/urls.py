from django.contrib import admin
from django.urls import path, include
from carteira.urls import CarteiraRouter
from compras.urls import ComprasRouter
from vendas.urls import VendasRouter
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('api/v1/', include(ComprasRouter.urls)),
    path('api/v1/', include(VendasRouter.urls)),
    path('api/v1/', include(CarteiraRouter.urls)),
    
    path('admin/', admin.site.urls),
    path('auth/', include('rest_framework.urls')),
    path('token/', obtain_auth_token, name='api_token_auth'),
    path('', include('frontend.urls'))
]


