from django.db import models

class Veiculo(models.Model):
    renavam = models.CharField(max_length=20)
    placa = models.CharField(max_length=10)
    proprietario = models.CharField(max_length=100)
    valor = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.renavam

class Notificacao(models.Model):
    veiculo = models.ForeignKey(Veiculo, on_delete=models.CASCADE)
    mensagem = models.TextField()
    data = models.DateTimeField(auto_now_add=True)

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