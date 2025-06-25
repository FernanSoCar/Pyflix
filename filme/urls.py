# Importações necessárias para configurar URLs
from django.contrib.auth import views as auth_views  # Views padrão de autenticação do Django
from django.urls import path, reverse_lazy  # Funções para definir URLs e reversão lazy
from .views import (  # Importa as views personalizadas da aplicação
    CriarConta,        # View para criação de conta
    EditarPerfil,      # View para edição de perfil
    FilmeDetailView,   # View para detalhes do filme
    HomeFilmesView,    # View da página principal de filmes
    HomePageView,      # View da página inicial
    PesquisaFilmeView, # View para pesquisa de filmes
)

# Define o namespace da aplicação para evitar conflitos de nomes
# Permite referenciar URLs como 'filme:homepage', 'filme:login', etc.
app_name = 'filme'

# Lista de padrões de URL da aplicação
urlpatterns = [
    # URL raiz da aplicação - Página inicial do site
    # Acesso: dominio.com/ (quando incluída como raiz no projeto principal)
    path('', HomePageView.as_view(), name='homepage'),
    
    # Página principal de filmes (área logada)
    # Acesso: dominio.com/filmes/
    path('filmes/', HomeFilmesView.as_view(), name='filmes'),
    
    # Página de detalhes de um filme específico
    # <int:pk> captura o ID do filme como parâmetro inteiro
    # Acesso: dominio.com/filmes/1/, dominio.com/filmes/2/, etc.
    path('filmes/<int:pk>/', FilmeDetailView.as_view(), name='filme_detalhes'),
    
    # Página de pesquisa de filmes
    # Acesso: dominio.com/pesquisa/?q=termo_pesquisa
    path('pesquisa/', PesquisaFilmeView.as_view(), name='pesquisa'),
    
    # Página de login usando a view padrão do Django
    # template_name especifica qual template usar
    # Acesso: dominio.com/login/
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    
    # Página de logout usando a view padrão do Django
    # Acesso: dominio.com/logout/
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    
    # Página de edição de perfil
    # <int:pk> captura o ID do usuário a ser editado
    # Acesso: dominio.com/editarperfil/1/
    path('editarperfil/<int:pk>/', EditarPerfil.as_view(), name='editar_perfil'),
    
    # Página de criação de nova conta
    # Acesso: dominio.com/criarconta/
    path('criarconta/', CriarConta.as_view(), name='criar_conta'),
    
    # Página para alterar senha usando view padrão do Django
    # success_url define para onde redirecionar após sucesso
    # reverse_lazy é usado para evitar problemas de importação circular
    # Acesso: dominio.com/mudar_senha/
    path('mudar_senha/', auth_views.PasswordChangeView.as_view(
        template_name='editarperfil.html', 
        success_url=reverse_lazy('filme:filmes')
    ), name='alterar_senha'),
]