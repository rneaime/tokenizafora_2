from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('criar_veiculo/', views.criar_veiculo, name='criar_veiculo'),
    path('tokenizar_veiculo/', views.tokenizar_veiculo, name='tokenizar_veiculo'),
    path('tokenizar_veiculo/<int:pk>/', views.tokenizar_veiculo, name='tokenizar_veiculo_pk'),
]