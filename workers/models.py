from django.db import models


# Modelo que representa a tabela que será criada no banco de dados pelo Django
class Workers(models.Model):
    nome = models.CharField(max_length=100)
    cargo = models.CharField(max_length=100)
    salario = models.FloatField()
    data_admissao = models.DateField()

    def __str__(self):
        return self.nome

