from django.contrib import admin
from .models import Veiculo, Notificacao, Permissao, Grupo, Usuario

admin.site.register(Veiculo)
admin.site.register(Notificacao)
admin.site.register(Permissao)
admin.site.register(Grupo)
admin.site.register(Usuario)
