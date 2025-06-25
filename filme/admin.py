# Importações necessárias para configurar o Django Admin
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin  # Admin padrão para usuários
from .models import Episodio, Filme, Usuario  # Modelos do app filme

# Personalização do UserAdmin para incluir o campo filmes_vistos
# Converte os fieldsets originais do UserAdmin de tupla para lista para permitir modificações
campos = list(UserAdmin.fieldsets)

# Adiciona uma nova seção "Histórico" com o campo filmes_vistos
# Este campo mostra quais filmes o usuário já assistiu
campos.append(
    ("Histórico", {"fields": ("filmes_vistos",)}),
)

# Converte de volta para tupla e substitui os fieldsets originais
# ATENÇÃO: Isso modifica globalmente a classe UserAdmin para todo o projeto
UserAdmin.fieldsets = tuple(campos)

# Registra os modelos no Django Admin para que apareçam na interface administrativa
admin.site.register(Filme)        # Permite administrar filmes
admin.site.register(Episodio)     # Permite administrar episódios
admin.site.register(Usuario, UserAdmin)  # Registra usuários com as configurações personalizadas
