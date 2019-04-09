from django.db import models


class Departamentos(models.Model):
    nome = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.nome
    

class CPF(models.Model):
    numero = models.CharField(max_length=15)
    data_exp = models.DateTimeField(auto_now=False)

    def __str__(self):
        return self.numero


class Cliente(models.Model):
    nome = models.CharField(max_length=100, blank=False, null=False)
    endereco = models.CharField(max_length=200, blank=False, null=False)
    salario = models.DecimalField(max_digits=10, decimal_places=2)
    idade = models.IntegerField()
    email= models.EmailField()
    cpf = models.OneToOneField(CPF, on_delete=models.CASCADE, null=True, blank=True)
    data_cad = models.DateTimeField(auto_now=True)
    departamentos = models.ManyToManyField(Departamentos, null=True, blank=True)
    foto = models.ImageField(upload_to='cliente_fotos')

    def __str__(self):
        return self.nome

 
class Telefone(models.Model):
    numero = models.CharField(max_length=20, blank=False, null=False)
    descricao = models.CharField(max_length=80, blank=False, null=False)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, null=False)

    def __str__(self):
        return self.numero + ' - ' + self.descricao 

