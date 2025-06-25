# Importações necessárias para criar modelos Django
from django.contrib.auth.models import AbstractUser  # Modelo base para usuários personalizados
from django.db import models  # Classes base para campos de modelo
from django.utils import timezone  # Utilitários de data/hora do Django

# Lista de escolhas para categorias de filmes
# Formato: (valor_no_banco, valor_exibido_ao_usuário)
LISTA_CATEGORIAS = [
    ("ANALISES", "Análises"),          # Filmes de análise/review
    ("PROGRAMACAO", "Programação"),    # Conteúdo sobre programação
    ("APRESENTACAO", "Apresentação"),  # Apresentações e palestras
    ("OUTROS", "Outros"),              # Categoria genérica
]


# Definição dos modelos do banco de dados
class Filme(models.Model):
    """
    Modelo que representa um filme/vídeo na plataforma.
    
    Armazena informações básicas como título, categoria, visualizações,
    data de criação, duração, descrição e thumbnail.
    """
    
    # Campo de texto para o título do filme (máximo 100 caracteres)
    titulo = models.CharField(max_length=100)  # Título do filme
    
    # Campo de escolha para categoria (limitado às opções em LISTA_CATEGORIAS)
    categoria = models.CharField(
        max_length=50, choices=LISTA_CATEGORIAS
    )  # Categoria do filme
    
    # Campo numérico para contar visualizações (inicia em 0)
    visualizacoes = models.IntegerField(default=0)  # Contador de visualizações
    
    # Campo de data que usa a data atual como padrão
    data_criacao = models.DateField(default=timezone.now)  # Data de criação do filme
    
    # Campo numérico para duração em minutos
    duracao = models.IntegerField()  # Duração em minutos
    
    # Campo de texto longo para descrição detalhada do filme
    descricao = models.TextField()  # Descrição do filme
    
    # Campo para upload de imagem (salva na pasta thumb_filmes/)
    thumbnail = models.ImageField(
        upload_to="thumb_filmes/"
    )  # Imagem de thumbnail do filme

    def __str__(self):
        """
        Método que define como o objeto é representado como string.
        Retorna o título do filme quando o objeto é exibido.
        """
        return self.titulo

    class Meta:
        """
        Metadados do modelo que definem configurações adicionais.
        """
        verbose_name = "Filme"              # Nome singular no admin
        verbose_name_plural = "Filmes"      # Nome plural no admin
        ordering = ["titulo"]               # Ordenação padrão por título


class Episodio(models.Model):
    """
    Modelo que representa um episódio de um filme/série.
    
    Cada episódio está vinculado a um filme e contém título e link do vídeo.
    Relacionamento: Um filme pode ter vários episódios (1:N).
    """
    
    # Chave estrangeira que liga o episódio a um filme
    # CASCADE: se o filme for deletado, todos os episódios também são deletados
    # related_name: permite acessar episódios a partir do filme (filme.episodios.all())
    filme = models.ForeignKey(
        Filme, on_delete=models.CASCADE, related_name="episodios"
    )  # Relacionamento com o modelo Filme
    
    # Campo de texto para o título do episódio
    titulo = models.CharField(max_length=100)  # Título do episódio
    
    # Campo URL para armazenar o link do vídeo (valida formato de URL)
    link_video = models.URLField()  # Link do vídeo do episódio

    def __str__(self):
        """
        Representação string do episódio.
        Formato: "Nome do Filme - Título do Episódio"
        """
        return f"{self.filme.titulo} - {self.titulo}"

    class Meta:
        """
        Metadados do modelo Episodio.
        """
        verbose_name = "Episódio"           # Nome singular no admin
        verbose_name_plural = "Episódios"   # Nome plural no admin
        ordering = ["titulo"]               # Ordenação padrão por título


class Usuario(AbstractUser):
    """
    Modelo de usuário personalizado que estende o AbstractUser do Django.
    
    Herda todos os campos padrão (username, email, password, etc.) e adiciona
    funcionalidades específicas da aplicação, como histórico de filmes assistidos.
    """

    # Campo Many-to-Many que relaciona usuários com filmes assistidos
    # Um usuário pode assistir vários filmes e um filme pode ser assistido por vários usuários
    # As aspas em "Filme" evitam erro de referência circular (modelo ainda não foi definido)
    filmes_vistos = models.ManyToManyField("Filme")  # Filmes que o usuário já viu

    class Meta:
        """
        Metadados do modelo Usuario.
        """
        verbose_name = "Usuário"            # Nome singular no admin
        verbose_name_plural = "Usuários"    # Nome plural no admin
        ordering = ["username"]             # Ordenação padrão por nome de usuário
