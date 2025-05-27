from django.contrib import admin
from .models import Veiculo, Notificacao, Permissao, Grupo, Usuario

class VeiculoAdmin(admin.ModelAdmin):
    list_display = ('renavam', 'placa', 'proprietario', 'valor')
    search_fields = ('renavam', 'placa', 'proprietario')

admin.site.register(Veiculo, VeiculoAdmin)
admin.site.register(Notificacao)
admin.site.register(Permissao)
admin.site.register(Grupo)
admin.site.register(Usuario)