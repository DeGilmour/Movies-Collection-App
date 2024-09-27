Movie Collection App

This project is a web application that allows users to search for movies, view detailed information, and manage their personal movie collection (e.g., watched, favorite, watchlist). Users can register, log in, and keep track of their movie preferences.
Features

    User registration and authentication
    Search for movies using an external API
    View detailed information about movies
    Add movies to your personal collection (watched, favorite, watchlist)
    Update or remove movies from your collection

Technologies Used

    Flask: Micro web framework for Python
    SQLAlchemy: ORM for database interactions
    Flask-Login: Authentication and session management
    Bootstrap: Frontend framework for responsive design
    Pytest: Testing framework for Python

Setup Instructions
Prerequisites

    Python 3.x
    Flask
    Docker (optional, for containerization)

## Installation

Clone the repository:

    cd <repository-directory>

### Create a virtual environment and activate it:



#### For Linux/Mac
    python -m venv venv
    source venv/bin/activate

### For Windows
    venv\Scripts\activate

### Install the required dependencies:

    pip install -r requirements.txt

### Set up the environment variables for configuration: Create a .env file and add the following values:
    SECRET_KEY="<your_key>"
    API_KEY="<your_api_key>"
    TOKEN="<your_token>"

### Initialize the database:

    flask db init
    flask db migrate
    flask db upgrade

### Run the application
    flask run

Running Tests

To run the test suite using pytest:

    pytest test.py


Docker Setup (Optional)

### Build the Docker image:
    docker build -t movie-collection-app .

### Run the Docker container:
    docker run -p 5000:5000 \
    -e SECRET_KEY="my_secret_key" \
    -e API_KEY="my_api_key" \
    -e TOKEN="my_token" \
    movie-collection-app



# Aplicativo de Coleção de Filmes

Este projeto é um aplicativo web que permite aos usuários pesquisar filmes, ver detalhes sobre os filmes e gerenciar sua coleção pessoal de filmes (assistidos, favoritos, lista de desejos). Os usuários podem se registrar, fazer login e acompanhar suas preferências de filmes.
Funcionalidades

    Registro e autenticação de usuários
    Pesquisa de filmes usando API externa
    Exibir informações detalhadas sobre os filmes
    Adicionar filmes à coleção pessoal (assistidos, favoritos, lista de desejos)
    Atualizar ou remover filmes da coleção

Tecnologias Utilizadas

    Flask: Microframework web para Python
    SQLAlchemy: ORM para interações com banco de dados
    Flask-Login: Autenticação e gerenciamento de sessões
    Bootstrap: Framework frontend para design responsivo
    Pytest: Framework de testes para Python

Instruções de Configuração
Pré-requisitos

    Python 3.x
    Flask
    Docker (opcional, para containerização)

## Instalação

#### Clone o repositório:
    git clone <repository-url>
    cd <repository-directory>

### Crie um ambiente virtual e ative-o:

# Para Linux/Mac
    python -m venv venv
    source venv/bin/activate

# Para Windows
venv\Scripts\activate

### Instale as dependências necessárias:

    pip install -r requirements.txt

###  Configure as variáveis de ambiente para configuração: 
Crie um arquivo .env e adicione os seguintes valores:

    SECRET_KEY="<sua_chave>"
    API_KEY="<sua_chave_api>"
    TOKEN="<sua_token>"
###  Inicialize o banco de dados:

    flask db init
    flask db migrate
    flask db upgrade

###  Execute o aplicativo:
    flask run

Executando os Testes

###  Para executar a suíte de testes usando pytest:
    pytest test.py

Verifique se todos os testes passam antes da implantação ou do desenvolvimento adicional.
Configuração do Docker (Opcional)

### Construa a imagem Docker:
    docker build -t movie-collection-app .

### Execute o container Docker
    docker run -p 5000:5000 \
    -e SECRET_KEY="my_secret_key" \
    -e API_KEY="my_api_key" \
    -e TOKEN="my_token" \
    movie-collection-app
