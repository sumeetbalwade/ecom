from .views import SignIn, UserViewSet
from rest_framework import routers
from django.urls import path, include
from rest_framework import urlpatterns
from . import views

router = routers.DefaultRouter()
router.register(r'', views.UserViewSet, basename='CustomUser')

urlpatterns = [
    path('login/', views.SignIn, name='SignIn'),
    path('signout/<int:id>/', views.signout, name='signout'),
    path('', include(router.urls))

]
