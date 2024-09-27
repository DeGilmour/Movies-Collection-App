# Movie Collection App

This project is a web application that allows users to search for movies, view movie details, and manage their personal movie collection (e.g., watched, favorite, watchlist). Users can register, log in, and keep track of their movie preferences.
Features

    User registration and authentication
    Search for movies using external API
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

Installation

    Clone the repository:

    bash

Create a virtual environment and activate it:

bash

python -m venv venv
source venv/bin/activate  # For Linux/Mac
venv\Scripts\activate     # For Windows

Install the required dependencies:

bash

pip install -r requirements.txt

Set up the environment variables for configuration: Create a .env file and add the following values:

bash

FLASK_APP=app
FLASK_ENV=development
SECRET_KEY=your_secret_key

Initialize the database:

bash

flask db init
flask db migrate
flask db upgrade

Run the application:

bash

    flask run

Running Tests

    Run the test suite using pytest:

    bash

    pytest

    Ensure that the tests pass before deployment or further development.

Docker Setup (Optional)

    Build the Docker image:

    bash

docker build -t movie-collection-app .

Run the Docker container:

bash

    docker run -p 5000:5000 movie-collection-app



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

Instalação

    Clone o repositório:

    bash

Crie um ambiente virtual e ative-o:

bash

python -m venv venv
source venv/bin/activate  # Para Linux/Mac
venv\Scripts\activate     # Para Windows

Instale as dependências necessárias:

bash

pip install -r requirements.txt

Configure as variáveis de ambiente para configuração: Crie um arquivo .env e adicione os seguintes valores:

bash

FLASK_APP=app
FLASK_ENV=development
SECRET_KEY=sua_chave_secreta

Inicialize o banco de dados:

bash

flask db init
flask db migrate
flask db upgrade

Execute o aplicativo:

bash

    flask run

Executando os Testes

    Execute a suíte de testes usando pytest:

    bash

    pytest

    Verifique se os testes passam antes da implantação ou do desenvolvimento adicional.

Configuração do Docker (Opcional)

    Construa a imagem Docker:

    bash

docker build -t movie-collection-app .

Execute o container Docker:

bash

docker run -p 5000:5000 movie-collection-app