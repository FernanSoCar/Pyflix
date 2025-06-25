# Importa a classe base AppConfig do Django para configuração de aplicações
from django.apps import AppConfig


class FilmeConfig(AppConfig):
    """
    Configuração da aplicação 'filme'.
    
    Esta classe define as configurações específicas da aplicação filme,
    incluindo o tipo de campo de chave primária padrão e o nome da aplicação.
    """
    
    # Define o tipo de campo de chave primária padrão para modelos sem pk explícita
    # BigAutoField permite IDs maiores (64-bit) em comparação com AutoField (32-bit)
    default_auto_field = 'django.db.models.BigAutoField'
    
    # Nome da aplicação Django - deve corresponder ao nome da pasta do app
    # Usado pelo Django para identificar e referenciar esta aplicação
    name = 'filme'
