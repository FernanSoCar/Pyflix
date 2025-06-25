# 🎬 Pyflix - Clone do Netflix

Uma aplicação web inspirada no Netflix, desenvolvida com Django, que permite aos usuários navegar, assistir e gerenciar uma biblioteca de filmes e episódios.

## OBS: Os vídeos utilizados foram criados por IA e são fictícios, não correspondendo a conteúdos reais. São aleatórios e não possuem direitos autorais. São utilizados apenas para fins educacionais e de demonstração.


![Python](https://img.shields.io/badge/Python-3.8+-blue)
![Django](https://img.shields.io/badge/Django-5.2-green)
![License](https://img.shields.io/badge/License-MIT-yellow)
![Status](https://img.shields.io/badge/Status-Em%20Desenvolvimento-orange)

## 🚀 Deploy

🌐 **Acesse a aplicação:** [https://pyflix-netflix-clone.herokuapp.com](https://pyflix-netflix-clone.herokuapp.com)


## 📋 Índice

- [Sobre o Projeto](#sobre-o-projeto)
- [Funcionalidades](#funcionalidades)
- [Tecnologias Utilizadas](#tecnologias-utilizadas)
- [Pré-requisitos](#pré-requisitos)
- [Instalação](#instalação)
- [Configuração](#configuração)
- [Como Usar](#como-usar)
- [Estrutura do Projeto](#estrutura-do-projeto)
- [API Reference](#api-reference)
- [Screenshots](#screenshots)
- [Contribuição](#contribuição)
- [Licença](#licença)
- [Contato](#contato)

## 📖 Sobre o Projeto

O **Pyflix** é um clone funcional do Netflix desenvolvido como projeto educacional utilizando Django. A aplicação oferece uma experiência completa de streaming, incluindo autenticação de usuários, navegação por catálogo de filmes, sistema de visualizações e recomendações.

### 🎯 Objetivos do Projeto

- Demonstrar habilidades em desenvolvimento web com Django
- Implementar sistema completo de autenticação e autorização
- Criar interface responsiva similar ao Netflix
- Desenvolver sistema de recomendações baseado em categoria
- Implementar upload e gerenciamento de arquivos de mídia

## ✨ Funcionalidades

### 🔐 Autenticação e Usuários
- ✅ Registro de novos usuários
- ✅ Login/Logout seguro
- ✅ Verificação inteligente de email (login vs registro)
- ✅ Edição de perfil
- ✅ Alteração de senha
- ✅ Sistema de usuários personalizados

### 🎬 Gestão de Filmes
- ✅ Catálogo completo de filmes
- ✅ Categorização por tipo (Análises, Programação, Apresentação, Outros)
- ✅ Sistema de episódios para séries
- ✅ Upload de thumbnails
- ✅ Contador de visualizações
- ✅ Histórico de filmes assistidos

### 🔍 Navegação e Descoberta
- ✅ Página inicial com filme em destaque
- ✅ Listagem de filmes recentes
- ✅ Seção "Em Alta" (mais visualizados)
- ✅ Sistema de busca por título
- ✅ Recomendações baseadas em categoria
- ✅ Interface responsiva

### 👤 Experiência do Usuário
- ✅ Dashboard personalizado
- ✅ Histórico de visualizações
- ✅ Filmes relacionados
- ✅ Interface intuitiva similar ao Netflix
- ✅ Navegação fluida entre páginas

## 🛠️ Tecnologias Utilizadas

### Backend
- **Python 3.8+** - Linguagem de programação
- **Django 5.2** - Framework web
- **PostgreSQL** - Banco de dados (desenvolvimento)
- **Pillow** - Processamento de imagens
- **Django Admin** - Interface administrativa

### Frontend
- **HTML5** - Estrutura das páginas
- **CSS3** - Estilização e layout
- **JavaScript** - Interatividade
- **Bootstrap** (opcional) - Framework CSS responsivo
- **Tailwind CSS** - Framework CSS utilitário

### Ferramentas de Desenvolvimento
- **uv** - Gerenciador de dependências Python
- **Git** - Controle de versão
- **VS Code** - IDE de desenvolvimento

## 📋 Pré-requisitos

Antes de começar, você precisará ter instalado em sua máquina:

- **Python 3.8 ou superior**
- **pip** (gerenciador de pacotes Python)
- **Git** (para clonar o repositório)
- **uv** (recomendado para gerenciamento de dependências)

## 🚀 Instalação

### 1. Clone o repositório
```bash
git clone https://github.com/FernanSoCar/Pyflix.git
cd Pyflix
```

### 2. Crie um ambiente virtual
```bash
# Usando uv (recomendado)
uv venv
uv pip sync

# Ou usando Python padrão
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate  # Windows
```

### 3. Instale as dependências
```bash
# Se usando uv
uv pip install -r requirements.txt

# Se usando pip
pip install -r requirements.txt
```

### 4. Configure o banco de dados
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Crie um superusuário
```bash
python manage.py createsuperuser
```

### 6. Execute o servidor de desenvolvimento
```bash
python manage.py runserver
```

Acesse `http://127.0.0.1:8000` em seu navegador.

## ⚙️ Configuração

### Variáveis de Ambiente

Crie um arquivo `.env` na raiz do projeto:

```env
SECRET_KEY=sua_secret_key_aqui
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

# Configurações de Banco de Dados (Produção)
DATABASE_URL=postgresql://user:password@localhost:5432/pyflix

# Configurações de Mídia
MEDIA_URL=/media/
STATIC_URL=/static/
```

### Configurações de Mídia

Para upload de thumbnails, certifique-se de que as pastas existam:

```bash
mkdir media
mkdir media/thumb_filmes
mkdir static
```

## 📱 Como Usar

### Para Usuários

1. **Registro/Login**
   - Acesse a página inicial
   - Digite seu email
   - Se for novo usuário, será direcionado para criação de conta
   - Se já for usuário, será direcionado para login

2. **Navegação**
   - Explore o catálogo na página principal
   - Use a barra de pesquisa para encontrar filmes específicos
   - Clique em um filme para ver detalhes

3. **Assistir Filmes**
   - Na página de detalhes, clique no episódio desejado
   - O filme será adicionado automaticamente ao seu histórico
   - Veja recomendações de filmes similares

### Para Administradores

1. **Acesse o painel admin**
   ```
   http://127.0.0.1:8000/admin/
   ```

2. **Gerenciar Filmes**
   - Adicione novos filmes com thumbnails
   - Configure categorias e episódios
   - Monitore visualizações

3. **Gerenciar Usuários**
   - Visualize usuários registrados
   - Veja histórico de filmes assistidos
   - Gerencie permissões

## 📁 Estrutura do Projeto

```
Copia_Netflix/
├── 📁 filme/                    # App principal
│   ├── 📄 admin.py             # Configuração do admin
│   ├── 📄 apps.py              # Configuração da app
│   ├── 📄 context_processors.py# Processadores de contexto
│   ├── 📄 forms.py             # Formulários
│   ├── 📄 models.py            # Modelos de dados
│   ├── 📄 urls.py              # URLs da app
│   ├── 📄 views.py             # Views/Controllers
│   ├── 📁 templates/           # Templates HTML
│   ├── 📁 migrations/          # Migrações do banco
│   └── 📁 __pycache__/         # Cache Python
├── 📁 Pyflix/                   # Configurações do projeto
│   ├── 📄 settings.py          # Configurações Django
│   ├── 📄 urls.py              # URLs principais
│   ├── 📄 wsgi.py              # WSGI para produção
│   └── 📄 asgi.py              # ASGI para async
├── 📁 media/                    # Arquivos de mídia
│   └── 📁 thumb_filmes/        # Thumbnails dos filmes
├── 📁 static/                   # Arquivos estáticos
│   ├── 📁 css/                 # Estilos CSS
│   ├── 📁 js/                  # Scripts JavaScript
│   └── 📁 images/              # Imagens do layout
├── 📁 templates/                # Templates globais
├── 📄 manage.py                # Utilitário Django
├── 📄 pyproject.toml           # Configurações do projeto
├── 📄 uv.lock                  # Lock file das dependências
└── 📄 README.md                # Este arquivo
```

## 🔧 API Reference

### Principais URLs

| Endpoint | Método | Descrição | Autenticação |
|----------|--------|-----------|--------------|
| `/` | GET | Página inicial | Não |
| `/filmes/` | GET | Lista de filmes | Sim |
| `/filmes/<id>/` | GET | Detalhes do filme | Sim |
| `/pesquisa/?q=<termo>` | GET | Buscar filmes | Sim |
| `/login/` | GET/POST | Login | Não |
| `/logout/` | POST | Logout | Sim |
| `/criarconta/` | GET/POST | Criar conta | Não |
| `/editarperfil/<id>/` | GET/POST | Editar perfil | Sim |
| `/admin/` | GET | Painel admin | Admin |

### Modelos de Dados

#### Filme
```python
{
    "id": 1,
    "titulo": "Nome do Filme",
    "categoria": "OUTROS",
    "visualizacoes": 150,
    "data_criacao": "2024-01-15",
    "duracao": 120,
    "descricao": "Descrição do filme...",
    "thumbnail": "thumb_filmes/filme1.jpg"
}
```

#### Usuário
```python
{
    "id": 1,
    "username": "usuario",
    "email": "usuario@email.com",
    "first_name": "João",
    "last_name": "Silva",
    "filmes_vistos": [1, 2, 3]
}
```

## 📸 Screenshots

### Página Inicial
![Homepage](docs/screenshots/homepage.png)

### Catálogo de Filmes
![Catalogo](docs/screenshots/catalogo.png)

### Detalhes do Filme
![Detalhes](docs/screenshots/detalhes.png)

### Painel Admin
![Admin](docs/screenshots/admin.png)

*Nota: Adicione as imagens na pasta `docs/screenshots/`*

## 🤝 Contribuição

Contribuições são sempre bem-vindas! Para contribuir:

1. **Fork** o projeto
2. Crie uma **branch** para sua feature (`git checkout -b feature/AmazingFeature`)
3. **Commit** suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. **Push** para a branch (`git push origin feature/AmazingFeature`)
5. Abra um **Pull Request**

### Diretrizes de Contribuição

- Mantenha o código limpo e bem documentado
- Adicione testes para novas funcionalidades
- Siga as convenções do Django
- Atualize a documentação quando necessário

## 📋 To-Do List

### Próximas Funcionalidades
- [ ] Sistema de avaliações (likes/dislikes)
- [ ] Comentários em filmes
- [ ] Playlists personalizadas
- [ ] Sistema de notificações
- [ ] Modo escuro/claro
- [ ] API REST para mobile
- [ ] Sistema de favoritos
- [ ] Recomendações baseadas em IA
- [ ] Integração com redes sociais
- [ ] Sistema de assinatura/planos

### Melhorias Técnicas
- [ ] Testes unitários e de integração
- [ ] Cache com Redis
- [ ] Docker e Docker Compose
- [ ] CI/CD com GitHub Actions
- [ ] Monitoring e logging
- [ ] Otimização de performance
- [ ] PWA (Progressive Web App)

## 🐛 Problemas Conhecidos

- Upload de vídeos grandes pode ser lento
- Interface pode não funcionar perfeitamente em navegadores muito antigos
- Sem suporte a streaming de vídeo em tempo real

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.


**Link do Projeto:** [https://github.com/seu-usuario/pyflix-netflix-clone](https://github.com/seu-usuario/pyflix-netflix-clone)

---

## 🎯 Aprendizados

Este projeto foi desenvolvido como parte do curso "Python Impressionador" e abrange:

- **Django Framework**: Views, Models, Templates, Forms
- **Autenticação**: Sistema completo de usuários
- **ORM**: Relacionamentos de banco de dados
- **Frontend**: HTML, CSS, JavaScript responsivo
- **Deploy**: Configuração para produção
- **Boas Práticas**: Código limpo e documentação

---

**⭐ Se este projeto te ajudou, deixe uma estrela no repositório!**

---

*Feito com Django*