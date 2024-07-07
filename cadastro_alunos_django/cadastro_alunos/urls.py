from django.contrib import admin
from django.urls import path
from cadastro import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('cadastrar_aluno/', views.cadastrar_aluno, name='cadastrar_aluno'),
    path('alunos/', views.alunos, name='alunos'),
    path('aluno/<int:pk>/', views.editar_aluno, name='editar_aluno'),
    path('deletar_aluno/<int:pk>/', views.deletar_aluno, name='deletar_aluno'),
]
