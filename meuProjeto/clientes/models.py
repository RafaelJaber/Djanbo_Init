from django.db import models


class Cliente(models.Model):
    nome = models.CharField(max_length=100, blank=False, null=False)
    endereco = models.CharField(max_length=200, blank=False, null=False)
    salario = models.DecimalField(max_digits=10, decimal_places=2)
    idade = models.IntegerField()
    email= models.EmailField()

    def __str__(self):
        return self.nome