from django.shortcuts import render, redirect
from .models import Veiculo, Notificacao, Permissao, Grupo, Usuario
from .forms import VeiculoForm, RegistroForm, LoginForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import PasswordResetView
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.models import Permission

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

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('index')

def registro_view(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = RegistroForm()
    return render(request, 'registro.html', {'form': form})

def notificacoes(request):
    notificacoes = Notificacao.objects.all()
    return render(request, 'notificacoes.html', {'notificacoes': notificacoes})

def permissoes(request):
    permissoes = Permissao.objects.all()
    return render(request, 'permissoes.html', {'permissoes': permissoes})

def grupos(request):
    grupos = Grupo.objects.all()
    return render(request, 'grupos.html', {'grupos': grupos})

def usuarios(request):
    usuarios = Usuario.objects.all()
    return render(request, 'usuarios.html', {'usuarios': usuarios})