from django.urls import path

from . import views

urlpatterns = [
    path('', views.principal, name= 'PaginaPrincipal'),
    #127.0.0.1:8000/livros/listar
    path('listar/', views.listar, name='listar'),
    path('listar_livros/', views.listar_livros, name='listarLivros'),
    #127.0.0.1:8000/livros/id
    path('<int:id>/', views.detail, name='detail'),
    #127.0.0.1:8000/livros/excluir/88
    path('excluir/<int:id>/', views.excluir, name='excluir'),
    #127.0.0.1:8000/livros/criar
    path('criar/', views.criar, name='criar'),
    #127.0.0.1:8000/livros/editar/88
    path('editar/<int:id>/', views.editar, name='editar'),

    path('meusLivros/', views.meusLivros, name='meusLivros'),
    path('agendados/', views.agendados, name='agendados'),
    path('devolvidos/', views.devolvidos, name='devolvidos'),
    path('buscar_livro', views.buscar_livro, name='buscar_livro'),
]