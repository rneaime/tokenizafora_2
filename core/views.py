from django.shortcuts import render
from .models import Veiculo


def index(request):
    veiculos = Veiculo.objects.all()
    return render(request, 'index.html', {'veiculos': veiculos})