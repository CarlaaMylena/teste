from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_filmes, name='listar_filmes'),
    path('novo/', views.criar_filme, name='criar_filme'),
    path('editar/<int:pk>/', views.editar_filme, name='editar_filme'),
    path('deletar/<int:pk>/', views.deletar_filme, name='deletar_filme'),
    path('buscar/', views.buscar_filme_omdb, name='buscar_filme_omdb'),
]