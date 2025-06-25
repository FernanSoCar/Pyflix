# Importações necessárias para criar formulários Django
from django import forms
from django.contrib.auth.forms import UserCreationForm  # Formulário base para criação de usuários
from .models import Usuario  # Modelo personalizado de usuário


class HomePageForm(forms.Form):
    """
    Formulário simples para capturar email na página inicial.
    
    Usado na homepage para verificar se o usuário já possui conta
    ou precisa criar uma nova conta no sistema.
    """
    # Campo de email sem label (label=False remove o texto do rótulo)
    # max_length=254 é o tamanho máximo padrão para emails
    email = forms.EmailField(max_length=254, label=False)


class CriarContaForm(UserCreationForm):
    """
    Formulário para criação de novas contas de usuário.
    
    Estende o UserCreationForm padrão do Django adicionando
    o campo de email como obrigatório.
    """
    # Campo de email adicional com validação e texto de ajuda
    email = forms.EmailField(
        max_length=254, help_text="Obrigatório. Informe um endereço de email válido."
    )

    class Meta:
        """
        Configuração do formulário especificando o modelo e campos.
        """
        model = Usuario  # Usa o modelo Usuario personalizado
        fields = (
            "username",    # Nome de usuário
            "email",       # Email do usuário
            "password1",   # Senha
            "password2",   # Confirmação da senha
        )


class LoginForm(forms.Form):
    """
    Formulário personalizado para login de usuários.
    
    Nota: Este formulário não está sendo usado atualmente.
    O projeto usa LoginView do Django que tem seu próprio formulário.
    """
    # Campo para nome de usuário
    username = forms.CharField()
    
    # Campo para senha com widget PasswordInput para ocultar os caracteres
    password = forms.CharField(widget=forms.PasswordInput())
