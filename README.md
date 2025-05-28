# Djanqguinho 🎯  (Em Construção)

## Sobre o Projeto  
O **Djanguinho** é uma plataforma web de streaming que terá intregração com blockchain, é um projeto de estudo para a Transfero Academy.

### 🧪 Exemplo Prático  
O usuário acessa a plataforma e escolhe um vídeo, depois de assistir ele poderá avaliá-lo e isso gerará um prêmio em moeda crupto.

---

## Funcionalidades Principais  

- 📊 Catálogo de filmes  
- 📈 Níveis de participação dos usuários (futuramente)
- 🎯 Avaliação remunerada em Crypto 
- 🔐 Autenticação simplificada com Google (futuramente)  
- Open Gov e financiamento de mídias (futuramente)
---

## Tecnologias Utilizadas  

### Backend  
- Python 3.13  
- Django 5.2  
- Django AllAuth (Autenticação Social)  (futuramente)
- SQLite3 (Banco de Dados)  (provisório)

### Frontend  
- HTML5  
- CSS3  
- Bootstrap 5   

---


## 🚀 Como Executar o Projeto  

### 1. Clone o repositório    
`git clone https://github.com/seu-usuario/DevMap.git`
`cd DevMap`

# Criar ambiente virtual  
`python -m venv venv`

# Ativar ambiente virtual (Windows)  
`venv\Scripts\activate`  

# Instalar dependências
`pip install -r requirements.txt`

# Aplicar as migrações
`python manage.py migrate`

# Executar o projeto
`python manage.py runserver` 


🔐 Configuração do Google OAuth (Futuramente)
# Acesse o Google Cloud Console
Crie um novo projeto

Vá em APIs e Serviços > Credenciais

Crie um novo ID do cliente OAuth 2.0 com o tipo Aplicativo Web

Configure os URIs de redirecionamento autorizados:


http://localhost:8000/accounts/google/login/callback/
No Django Admin
Acesse http://localhost:8000/admin

Em Sites, adicione localhost:8000

Em Social Applications:

Provedor: Google

Nome: Google

ID do Cliente: (insira o ID do Google Cloud)

Chave Secreta: (insira a chave secreta do Google Cloud)

Sites: selecione localhost:8000


📝 Licença
Este projeto está sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.
