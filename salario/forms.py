from django import forms
from .models import Salario

class SalarioForm(forms.ModelForm):
    class Meta:
        model = Salario
        fields = '__all__' # Ou especifique os campos que você quer usar: ['valor', 'anos_de_trabalho', ...]
        
        # Opcional: personalize widgets e labels para Bootstrap
        widgets = {
            # Adicione a classe 'form-control' para o estilo do Bootstrap
            'valor': forms.NumberInput(attrs={'step': '0.01', 'class': 'form-control'}),
            'anos_de_trabalho': forms.NumberInput(attrs={'class': 'form-control'}),
            # Se você tiver um campo 'data' no seu modelo Salario:
            # 'data': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }
        
        labels = {
            'valor': 'Valor do Salário',
            'anos_de_trabalho': 'Anos de Trabalho',
            # 'data': 'Data do Pagamento', # Se 'data' for um campo
        }

