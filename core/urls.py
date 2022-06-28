from django.urls import path
from . import views



urlpatterns = [
    path('', views.home, name="home"),
    path('treinamentos/', views.treinamentos, name='treinamentos'),
    path('treinamento/<int:id>/', views.treinamentos, name='treinamento-detalhe')
]