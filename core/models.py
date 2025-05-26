from django.db import models

class Veiculo(models.Model):
    renavam = models.CharField(max_length=20)
    placa = models.CharField(max_length=10)
    proprietario = models.CharField(max_length=100)
    valor = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.renavam