from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar, name='salario_pessoa_listar'),
    path('novo/', views.criar, name='salario_pessoa_criar'),
    path('editar/<int:pk>/', views.editar, name='salario_pessoa_editar'),
    path('deletar/<int:pk>/', views.deletar, name='salario_pessoa_deletar'),
]