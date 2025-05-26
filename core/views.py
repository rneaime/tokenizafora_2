from django.shortcuts import render, redirect
from .models import Veiculo
from .forms import VeiculoForm
import jwt
import datetime


def index(request):
    veiculos = Veiculo.objects.all()
    return render(request, 'index.html', {'veiculos': veiculos})

def criar_veiculo(request):
    if request.method == 'POST':
        form = VeiculoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = VeiculoForm()
    return render(request, 'criar_veiculo.html', {'form': form})

def tokenizar_veiculo(request, pk=None):
    if request.method == 'POST':
        veiculo_id = request.POST.get('veiculo_id')
        valor = request.POST.get('valor')
        veiculo = Veiculo.objects.get(id=veiculo_id)
        # Gere o token JWT
        payload = {
            'veiculo_id': veiculo.id,
            'renavam': veiculo.renavam,
            'placa': veiculo.placa,
            'proprietario': veiculo.proprietario,
            'valor': valor,
            'exp': int(datetime.datetime.now().timestamp()) + 3600
        }
        token = jwt.encode(payload, 'minha_chave_secreta', algorithm='HS256')
        return render(request, 'tokenizar_veiculo.html', {'token': token, 'veiculo': veiculo})
    else:
        if pk:
            veiculo = Veiculo.objects.get(id=pk)
            return render(request, 'tokenizar_veiculo.html', {'veiculo': veiculo})
        else:
            return render(request, 'tokenizar_veiculo.html')
