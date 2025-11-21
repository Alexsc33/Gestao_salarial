from django.db import models

class Salario(models.Model):
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    anos_de_trabalho = models.PositiveSmallIntegerField(verbose_name='Anos de Trabalho')

    def __str__(self):
        return f'{self.valor} - {self.anos_de_trabalho} anos'