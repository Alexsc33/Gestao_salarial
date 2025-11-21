from django import forms
from .models import SalarioPessoa

class SalarioPessoaForm(forms.ModelForm):
    class Meta:
        model = SalarioPessoa
        fields = '__all__'