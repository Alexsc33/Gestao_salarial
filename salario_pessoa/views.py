from django.shortcuts import render, redirect, get_object_or_404
from .models import SalarioPessoa
from .forms import SalarioPessoaForm
from django.contrib.auth.decorators import login_required, permission_required

@login_required
def listar(request):
    relacoes = SalarioPessoa.objects.all()
    return render(request, 'salario_pessoa/listar.html', {'relacoes': relacoes})

@login_required
@permission_required('salario_pessoa.add_salario_pessoa', raise_exception=True)
def criar(request):
    if request.method == 'POST':
        form = SalarioPessoaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('salario_pessoa_listar')
    else:
        form = SalarioPessoaForm()
    return render(request, 'salario_pessoa/form.html', {'form': form})

@login_required
@permission_required('salario_pessoa.view_salario_pessoa', raise_exception=True)
def editar(request, pk):
    relacao = get_object_or_404(SalarioPessoa, pk=pk)
    if request.method == 'POST':
        form = SalarioPessoaForm(request.POST, instance=relacao)
        if form.is_valid():
            form.save()
            return redirect('salario_pessoa_listar')
    else:
        form = SalarioPessoaForm(instance=relacao)
    return render(request, 'salario_pessoa/form.html', {'form': form})

@login_required
@permission_required('salario_pessoa.delete_salario_pessoa', raise_exception=True)
def deletar(request, pk):
    relacao = get_object_or_404(SalarioPessoa, pk=pk)
    if request.method == 'POST':
        relacao.delete()
        return redirect('salario_pessoa_listar')
    return render(request, 'salario_pessoa/deletar.html', {'relacao': relacao})
