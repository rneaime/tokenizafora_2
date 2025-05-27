from django.shortcuts import render
from .models import Veiculo

def index(request):
    veiculos = Veiculo.objects.all()
    busca = request.GET.get('busca')
    if busca:
        veiculos = veiculos.filter(marca__icontains=busca) | veiculos.filter(modelo__icontains=busca) | veiculos.filter(placa__icontains=busca)
    return render(request, 'index.html', {'veiculos': veiculos})