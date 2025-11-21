from django import forms
from .models import Contato

class ContatoForm(forms.ModelForm):
    
    class Meta:
        model = Contato
        fields = ['nome', 'email', 'cpf', 'idade']

        widgets = {
            'nome': forms.TextInput(attrs={'placeholder': 'Digite seu nome'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Digite seu email'}),
            'cpf': forms.TextInput(attrs={'placeholder': 'Digite seu CPF'}),
            'idade': forms.NumberInput(attrs={'placeholder': 'Digite sua idade'}),
        }
