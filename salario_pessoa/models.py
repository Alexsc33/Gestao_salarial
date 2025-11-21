from django.db import models
from pessoa.models import Contato
from salario.models import Salario

class SalarioPessoa(models.Model):
    pessoa = models.ForeignKey(Contato, on_delete=models.CASCADE)
    salario = models.ForeignKey(Salario, on_delete=models.CASCADE)
    data_inicio = models.DateField(null=True, blank=True)
    data_fim = models.DateField(null=True, blank=True)

    class Meta:
        unique_together = ('pessoa', 'salario')

    def __str__(self):
        return f"{self.pessoa.nome} - {self.salario.valor}"