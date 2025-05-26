from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('criar_veiculo/', views.criar_veiculo, name='criar_veiculo'),
]