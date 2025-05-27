from django import forms
from .models import Veiculo, Usuario
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm

class VeiculoForm(forms.ModelForm):
    class Meta:
        model = Veiculo
        fields = ('marca', 'modelo', 'ano', 'placa', 'cor', 'proprietario', 'valor_mercado', 'renavam')
        
    def clean_renavam(self):
        renavam = self.cleaned_data['renavam']
        if len(renavam) != 11:
            raise ValidationError('O RENAVAM deve ter 11 dígitos')
        return renavam


class LoginForm(forms.Form):
    username = forms.CharField(label='Nome de usuário', max_length=100)
    password = forms.CharField(label='Senha', widget=forms.PasswordInput)


class RegistroForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = Usuario
        fields = ('username', 'email', 'password1', 'password2')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if Usuario.objects.filter(email=email).exists():
            raise ValidationError('Este email já está em uso.')
        return email

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
