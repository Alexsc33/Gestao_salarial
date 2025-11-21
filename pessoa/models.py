from django.db import models

class Contato(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    cpf = models.CharField(max_length=14, unique=True, null=True, blank=True)    
    idade = models.PositiveIntegerField()
    salarios = models.ManyToManyField(
        'salario.Salario',
        through='salario_pessoa.SalarioPessoa',
        related_name='pessoas'
    )

    def __str__(self):
        return self.nome
