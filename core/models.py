from django.db import models
from django.contrib.auth.models import AbstractUser

class Veiculo(models.Model):
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    ano = models.IntegerField()
    placa = models.CharField(max_length=10)
    cor = models.CharField(max_length=30)
    proprietario = models.ForeignKey('Usuario', on_delete=models.CASCADE, related_name='veiculos')
    valor_mercado = models.DecimalField(max_digits=10, decimal_places=2)
    renavam = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.marca} {self.modelo} - {self.placa}"

    class Meta:
        verbose_name = 'Veículo'
        verbose_name_plural = 'Veículos'

class Notificacao(models.Model):
    veiculo = models.ForeignKey(Veiculo, on_delete=models.CASCADE)
    usuario = models.ForeignKey('Usuario', on_delete=models.CASCADE, related_name='notificacoes')
    mensagem = models.TextField()
    data = models.DateTimeField(auto_now_add=True)
    lida = models.BooleanField(default=False)

    def __str__(self):
        return self.mensagem

class Permissao(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()

    def __str__(self):
        return self.nome

class Grupo(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    permissoes = models.ManyToManyField(Permissao)

    def __str__(self):
        return self.nome

class Usuario(AbstractUser):
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    grupos = models.ManyToManyField(Grupo)
    permissao = models.ForeignKey(Permissao, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.username
        
    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'
        swappable = 'AUTH_USER_MODEL'
