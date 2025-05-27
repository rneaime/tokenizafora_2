from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('criar_veiculo/', views.criar_veiculo, name='criar_veiculo'),
    path('tokenizar_veiculo/', views.tokenizar_veiculo, name='tokenizar_veiculo'),
    path('tokenizar_veiculo/<int:pk>/', views.tokenizar_veiculo, name='tokenizar_veiculo_pk'),
    path('notificacoes/', views.notificacoes, name='notificacoes'),
    path('permissoes/', views.permissoes, name='permissoes'),
    path('grupos/', views.grupos, name='grupos'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('registro/', views.registro_view, name='registro'),
]