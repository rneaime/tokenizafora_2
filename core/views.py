from django.shortcuts import render, redirect
from .models import Veiculo
from .forms import VeiculoForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
import jwt
import datetime
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import logout
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.views import PasswordResetView

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
    try:
        veiculo = Veiculo.objects.get(id=pk)
    except ObjectDoesNotExist:
        return render(request, 'tokenizar_veiculo.html', {'erro': 'Veículo não encontrado'})
    if request.method == 'POST':
        veiculo_id = request.POST.get('veiculo_id')
        valor = request.POST.get('valor')
        # Gere o token JWT
        payload = {
            'veiculo_id': veiculo.id,
            'renavam': veiculo.renavam,
            'placa': veiculo.placa,
            'proprietario': veiculo.proprietario,
            'valor': valor,
            'exp': int(datetime.datetime.now().timestamp()) + 3600
        }
        token = jwt.encode(payload, 'chave_secreta_aleatoria', algorithm='HS256')
        return render(request, 'tokenizar_veiculo.html', {'token': token, 'veiculo': veiculo})
    else:
        return render(request, 'tokenizar_veiculo.html', {'veiculo': veiculo})

def logout_view(request):
    logout(request)
    return redirect('index')

def recuperar_senha(request):
    if request.method == 'POST':
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = PasswordResetForm()
    return render(request, 'recuperar_senha.html', {'form': form})

def editar_perfil(request):
    if request.method == 'POST':
        form = EditarPerfilForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = EditarPerfilForm(instance=request.user)
    return render(request, 'editar_perfil.html', {'form': form})
