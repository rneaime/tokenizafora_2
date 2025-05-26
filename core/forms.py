from django import forms
from .models import Veiculo
from django.core.exceptions import ValidationError

class VeiculoForm(forms.ModelForm):
    class Meta:
        model = Veiculo
        fields = ('renavam', 'placa', 'proprietario', 'valor')
    def clean_renavam(self):
        renavam = self.cleaned_data['renavam']
        if len(renavam) != 11:
            raise ValidationError('O RENAVAM deve ter 11 dígitos')
        return renavam
