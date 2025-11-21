from django.urls import path

from . import views

urlpatterns = [
    path('novo/', views.create, name='create'),
    path('', views.list, name='list'),
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/editar/', views.update, name='update'),
    path('<int:pk>/excluir/', views.delete, name='delete'),
]