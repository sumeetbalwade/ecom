from django.urls import path
from django.urls.conf import include
from . import views as v

from rest_framework.authtoken import views
from rest_framework.authtoken.views import ObtainAuthToken

urlpatterns = [
    path('', v.home, name='api_home'),
    path('category/', include('api.category.urls')),
    path('product/', include('api.product.urls')),
    path('user/', include('api.user.urls')),
    path('order/', include('api.order.urls')),
    path('payment/', include('api.payment.urls')),
    path('api-token-auth/', ObtainAuthToken, name='api_token_auth')

]
