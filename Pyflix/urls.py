"""
URL configuration for Pyflix project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# Lista principal de padrões de URL do projeto
urlpatterns = [
    # URL para o painel administrativo do Django
    # Acesso: dominio.com/admin/
    path('admin/', admin.site.urls),
    
    # Inclui todas as URLs da aplicação 'filme' na raiz do site
    # namespace='filme' permite referenciar URLs como 'filme:homepage'
    # Todas as URLs de filme.urls ficam acessíveis diretamente na raiz
    # Ex: dominio.com/, dominio.com/filmes/, dominio.com/login/, etc.
    path('', include('filme.urls', namespace='filme')),
    
]


# Configuração para servir arquivos de mídia durante o desenvolvimento
# MEDIA_URL: URL base para arquivos de mídia (uploads, thumbnails, etc.)
# MEDIA_ROOT: Diretório físico onde os arquivos de mídia são armazenados
# Permite acesso a arquivos como dominio.com/media/thumb_filmes/filme1.jpg
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Configuração para servir arquivos estáticos durante o desenvolvimento
# STATIC_URL: URL base para arquivos estáticos (CSS, JS, imagens do layout)
# STATIC_ROOT: Diretório onde arquivos estáticos são coletados para produção
# Permite acesso a arquivos como dominio.com/static/css/style.css
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    