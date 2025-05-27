from django.contrib import admin
from .models import Veiculo
from .views import tokenizar_veiculo

class VeiculoAdmin(admin.ModelAdmin):
    list_display = ('renavam', 'placa', 'proprietario', 'valor_mercado')
    actions = ['gerar_token']

    def gerar_token(self, request, queryset):
        for veiculo in queryset:
            token = tokenizar_veiculo(request, veiculo.id)
            self.message_user(request, f'Token gerado para o ve\u00edculo {veiculo.renavam}')

admin.site.register(Veiculo, VeiculoAdmin)