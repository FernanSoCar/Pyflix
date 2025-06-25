# Importações necessárias para criar views Django
from django.contrib.auth.mixins import LoginRequiredMixin  # Mixin para views que requerem login
from django.shortcuts import redirect, reverse  # Funções para redirecionamento e reversão de URLs
from django.views.generic import (  # Views genéricas do Django para reutilização
    DetailView,    # View para exibir detalhes de um objeto
    FormView,      # View para processar formulários
    ListView,      # View para listar objetos
    UpdateView,    # View para atualizar objetos
)
from .forms import CriarContaForm, HomePageForm  # Formulários personalizados da aplicação
from .models import Filme, Usuario  # Modelos da aplicação


# Definição das views da aplicação
class HomePageView(FormView):
    """
    View da página inicial do site.
    
    Processa o formulário de email para direcionar usuários para login
    ou criação de conta. Se o usuário já estiver logado, redireciona
    diretamente para a página de filmes.
    """
    template_name = "homepage.html"  # Template a ser renderizado
    form_class = HomePageForm        # Formulário a ser usado

    def get(self, request, *args, **kwargs):
        """
        Sobrescreve o método GET para verificar autenticação.
        
        Se o usuário já estiver logado, redireciona para /filmes/
        caso contrário, exibe a página inicial normalmente.
        """
        if request.user.is_authenticated:
            return redirect("/filmes/")  # Redireciona usuário logado
        return super().get(request, *args, **kwargs)

    def get_success_url(self):
        """
        Define para onde redirecionar após envio bem-sucedido do formulário.
        
        Verifica se o email informado já existe no sistema:
        - Se existe: direciona para página de login
        - Se não existe: direciona para página de criação de conta
        """
        email = self.request.POST.get("email")  # Obtém email do formulário
        usuarios = Usuario.objects.filter(email=email)  # Busca usuários com esse email
        if usuarios.exists():
            return reverse("filme:login")        # Email existe -> login
        else:
            return reverse("filme:criar_conta")  # Email novo -> criar conta


class HomeFilmesView(LoginRequiredMixin, ListView):
    """
    View da página principal de filmes (área logada).
    
    Exibe a lista de todos os filmes disponíveis.
    Requer que o usuário esteja logado (LoginRequiredMixin).
    """
    model = Filme                           # Modelo a ser listado
    template_name = "homefilmes.html"       # Template a ser renderizado
    context_object_name = "lista_filmes"    # Nome da variável no template


class FilmeDetailView(LoginRequiredMixin, DetailView):
    """
    View para exibir detalhes de um filme específico.
    
    Além de exibir as informações do filme, também:
    - Incrementa o contador de visualizações
    - Adiciona o filme à lista de filmes vistos pelo usuário
    - Busca filmes relacionados da mesma categoria
    """
    model = Filme                       # Modelo a ser exibido
    template_name = "detalhesfilme.html" # Template a ser renderizado
    
    def get(self, request, *args, **kwargs):
        """
        Sobrescreve o método GET para registrar visualização.
        
        A cada acesso à página do filme:
        1. Incrementa contador de visualizações do filme
        2. Adiciona filme à lista de filmes vistos pelo usuário
        """
        filme = self.get_object()  # Obtém o filme pela pk da URL
        usuario = request.user     # Usuário atual logado
        
        # Incrementa contador de visualizações e salva no banco
        filme.visualizacoes += 1
        filme.save()
        
        # Adiciona filme à lista de filmes vistos (ManyToMany)
        # O .add() já salva automaticamente no banco
        usuario.filmes_vistos.add(filme)
        
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        """
        Adiciona dados extras ao contexto do template.
        
        Busca filmes relacionados (mesma categoria) para exibir
        como sugestões, excluindo o filme atual da lista.
        """
        context = super().get_context_data(**kwargs)
        
        # Busca filmes da mesma categoria, exclui o filme atual, limita a 5
        filmes_relacionados = Filme.objects.filter(
            categoria=self.object.categoria  # Mesma categoria do filme atual
        ).exclude(id=self.object.id)[0:5]    # Exclui filme atual, pega 5
        
        context["filmes_relacionados"] = filmes_relacionados
        return context


class PesquisaFilmeView(LoginRequiredMixin, ListView):
    """
    View para pesquisa de filmes.
    
    Permite aos usuários buscar filmes por título.
    Se não houver termo de pesquisa, retorna lista vazia.
    """
    model = Filme                    # Modelo a ser pesquisado
    template_name = "pesquisa.html"  # Template a ser renderizado
    context_object_name = "filmes"   # Nome da variável no template

    def get_queryset(self):
        """
        Define quais objetos serão listados baseado na pesquisa.
        
        Obtém o parâmetro 'q' da URL (?q=termo_pesquisa) e
        busca filmes cujo título contenha o termo (case-insensitive).
        """
        query = self.request.GET.get("q")  # Parâmetro de pesquisa da URL
        if query:
            # icontains = busca case-insensitive que contém o termo
            return Filme.objects.filter(titulo__icontains=query)
        return Filme.objects.none()  # Retorna queryset vazio se sem pesquisa


class EditarPerfil(LoginRequiredMixin, UpdateView):
    """
    View para edição de perfil do usuário.
    
    Permite ao usuário editar informações básicas como
    nome, sobrenome e email.
    """
    template_name = "editarperfil.html"              # Template a ser renderizado
    model = Usuario                                  # Modelo a ser editado
    fields = ["first_name", "last_name", "email"]   # Campos editáveis

    def get_success_url(self):
        """
        Define para onde redirecionar após edição bem-sucedida.
        
        Retorna para a página principal de filmes.
        """
        return reverse("filme:filmes")


class CriarConta(FormView):
    """
    View para criação de nova conta de usuário.
    
    Processa o formulário de criação de conta e,
    após sucesso, redireciona para a página de login.
    """
    template_name = "criarconta.html"  # Template a ser renderizado
    form_class = CriarContaForm        # Formulário a ser usado

    def get_success_url(self) -> str:
        """
        Define para onde redirecionar após criação bem-sucedida.
        
        Redireciona para a página de login para que o usuário
        possa fazer login com a conta recém-criada.
        """
        return reverse("filme:login")

    def form_valid(self, form):
        """
        Processa formulário válido.
        
        Salva o novo usuário no banco de dados e
        prossegue com o redirecionamento.
        """
        form.save()  # Cria o usuário no banco de dados
        return super().form_valid(form)
