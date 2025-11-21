from django.urls import path, include
from . import views
from .views import PessoaViewSet
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register(r'pessoas', PessoaViewSet)


urlpatterns = [
    path('contato/novo/', views.contato_create, name='contato_create'),
    path('', views.contato_list, name='contato_list'),
    path('contato/<int:pk>/', views.contato_detail, name='contato_detail'),
    path('contato/<int:pk>/editar/', views.contato_update, name='contato_update'),
    path('contato/<int:pk>/excluir/', views.contato_delete, name='contato_delete'),
    path('', include(router.urls)),
]