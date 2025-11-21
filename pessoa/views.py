from django.shortcuts import render, redirect, get_object_or_404
from .forms import ContatoForm
from .models import Contato 
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required, permission_required
from .serializers import PessoaSerializer
from rest_framework import viewsets



class PessoaViewSet(viewsets.ModelViewSet):
    queryset = Contato.objects.all()
    serializer_class = PessoaSerializer

@login_required
def home(request):
    return render(request, 'app/home.html')

@login_required
@permission_required('pessoa.add_contato', raise_exception=True)
def contato_create(request):
    if request.method == 'POST':
        form = ContatoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Contato criado com sucesso!')
            return redirect('contato_list')
    else:
        form = ContatoForm()
    return render(request, 'pessoa/contato_form.html', {'form': form, 'titulo': 'Novo Contato'})

@login_required
def contato_list(request):
    contatos = Contato.objects.all().order_by('-id')  # ou .order_by('nome')
    return render(request, 'pessoa/contato_list.html', {'contatos': contatos})

@login_required
def contato_detail(request, pk):
    contato = get_object_or_404(Contato, pk=pk)
    return render(request, 'pessoa/contato_detail.html', {'contato': contato})

@login_required
@permission_required('pessoa.change_contato', raise_exception=True)
def contato_update(request, pk):
    contato = get_object_or_404(Contato, pk=pk)
    if request.method == 'POST':
        form = ContatoForm(request.POST, instance=contato)
        if form.is_valid():
            form.save()
            messages.success(request, 'Contato atualizado com sucesso!')
            return redirect('contato_detail', pk=contato.pk)  # Corrigido aqui
    else:
        form = ContatoForm(instance=contato)
    return render(request, 'pessoa/contato_form.html', {'form': form, 'titulo': 'Editar Contato'})

@login_required
@permission_required('pessoa.delete_contato', raise_exception=True)
def contato_delete(request, pk):
    contato = get_object_or_404(Contato, pk=pk)
    if request.method == 'POST':
        contato.delete()
        messages.success(request, 'Contato excluido com sucesso!')
        return redirect('contato_list')
    return render(request, 'pessoa/contato_confirm_delete.html', {'contato': contato})