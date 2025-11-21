from django.shortcuts import render, redirect, get_object_or_404  # Adicione get_object_or_404 aqui
from .forms import SalarioForm
from .models import Salario  # Faltou importar o modelo Salario
from django.contrib import messages
from django.http import HttpResponse

from django import forms
from django.shortcuts import render

from django.contrib.auth.decorators import login_required, permission_required

@login_required
def home(request):
    return render(request, 'home.html')

@login_required
@permission_required('salario.add_salario', raise_exception=True)
def create(request):
    if request.method == 'POST':
        # Quando a requisição é POST, você passa apenas os dados do POST.
        # O objeto 'request.POST' JÁ é um dicionário que o formulário espera.
        form = SalarioForm(request.POST) # <-- Corrigido: Removido 'request' como primeiro argumento
        if form.is_valid():
            form.save()
            messages.success(request, 'Salário criado com sucesso!')
            return redirect('list')
    else:
        # Quando a requisição é GET (para exibir o formulário vazio pela primeira vez),
        # você simplesmente instancia o formulário sem argumentos.
        form = SalarioForm() # <-- Corrigido: Removido 'request' aqui
    return render(request, 'salario/form.html', {'form': form, 'titulo': 'Novo Salário'})

@login_required
def list(request):
    salarios = Salario.objects.all()
    return render(request, 'salario/list.html', {'salarios': salarios})  # Corrigi o caminho do template

@login_required
def detail(request, pk):
    salario = get_object_or_404(Salario, pk=pk)
    return render(request, 'salario/detail.html', {'salario': salario})  # Corrigi 'pesssoa' para 'salario'

@login_required
@permission_required('salario.change_salario', raise_exception=True)
def update(request, pk):
    salario = get_object_or_404(Salario, pk=pk)
    if request.method == 'POST':
        form = SalarioForm(request.POST, instance=salario)
        if form.is_valid():
            form.save()
            messages.success(request, 'Salario atualizado com sucesso!')
            return redirect('detail', pk=salario.pk)
    else:
        form = SalarioForm(instance=salario)
    return render(request, 'salario/form.html', {'form': form, 'titulo': 'Editar Salario'})

@login_required
@permission_required('salario.delete_salario', raise_exception=True)
def delete(request, pk):
    salario = get_object_or_404(Salario, pk=pk)
    if request.method == 'POST':
        salario.delete()
        messages.success(request, 'Salario excluido com sucesso!')
        return redirect('list')
    return render(request, 'salario/confirm_delete.html', {'salario': salario})