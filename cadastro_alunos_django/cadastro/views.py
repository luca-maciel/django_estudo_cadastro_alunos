from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .form import *
# Create your views here.

def home(request):
    return render(request, 'home.html')


def cadastrar_aluno(request):
    data = {}
    form = CadastroForm(request.POST or None)
    data['form'] = form
    if form.is_valid():
        form.save()
        return redirect('alunos')
    
    return render(request, 'cadastrar_aluno.html', data)

def alunos(request):
    data = {}
    data['alunos'] = Aluno.objects.all()
    return render(request, 'alunos.html', data)

def editar_aluno(request, pk):
    aluno = Aluno.objects.get(pk=pk)
    data = {}
    form = CadastroForm(request.POST or None, instance=aluno)
    data['form'] = form
    data['aluno'] = aluno
    data['existe'] = True
    if form.is_valid():
        form.save()
        return redirect('alunos')
    return render(request, 'cadastrar_aluno.html', data)

def deletar_aluno(request, pk):
    aluno = Aluno.objects.get(pk=pk)
    aluno.delete()
    return redirect('alunos')
    