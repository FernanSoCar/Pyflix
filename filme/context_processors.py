# Importa o modelo Filme para fazer consultas ao banco de dados
from .models import Filme

def lista_filmes_recentes(request):
    """
    Context processor que fornece uma lista dos filmes mais recentes.
    
    Este processador de contexto torna disponível em todos os templates
    uma lista dos 8 filmes mais recentemente adicionados ao sistema.
    """
    # Busca todos os filmes, ordena pela data de criação (mais recente primeiro) 
    # e limita aos primeiros 8 resultados
    filmes = Filme.objects.all().order_by('-data_criacao')[:8]  # Get the 8 most recent movies
    
    # Retorna um dicionário que será adicionado ao contexto de todos os templates
    return {'lista_filmes_recentes': filmes}

def lista_filmes_em_alta(request):
    """
    Context processor que fornece uma lista dos filmes mais populares.
    
    Este processador de contexto torna disponível em todos os templates
    uma lista dos 8 filmes com maior número de visualizações.
    """
    # Busca todos os filmes, ordena pelo número de visualizações (maior primeiro)
    # e limita aos primeiros 8 resultados
    filmes = Filme.objects.all().order_by('-visualizacoes')[:8]  # Get the 8 most viewed movies
    
    # Retorna um dicionário que será adicionado ao contexto de todos os templates
    return {'lista_filmes_em_alta': filmes}

def filme_destaque(request):
    """
    Context processor que fornece um filme em destaque.
    
    Este processador de contexto torna disponível em todos os templates
    o filme mais recentemente adicionado para ser usado como destaque principal.
    """
    # Busca o filme mais recente (primeiro na ordenação por data de criação descendente)
    # .first() retorna apenas o primeiro resultado ou None se não houver filmes
    filmes = Filme.objects.order_by('-data_criacao').first()  # Get the most recent movie
    
    # Retorna um dicionário que será adicionado ao contexto de todos os templates
    return {'filme_destaque': filmes}