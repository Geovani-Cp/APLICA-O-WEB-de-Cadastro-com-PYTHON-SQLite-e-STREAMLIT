Aplicação Web de Cadastro com Python, SQLite e Streamlit
Uma aplicação web simples para cadastro de clientes, desenvolvida com Python, utilizando o Streamlit para a interface e o SQLite como banco de dados.

Sobre o Projeto
Este projeto demonstra a criação de uma aplicação web interativa onde o usuário pode cadastrar, listar e gerenciar informações de clientes. O projeto é ideal para quem está começando a trabalhar com a biblioteca Streamlit e quer entender como integrá-la a um banco de dados local.

Funcionalidades
Cadastro de Clientes: Formulário simples para inserção de novos clientes.

Listagem de Clientes: Exibição dos clientes cadastrados em uma tabela interativa.

Banco de Dados Local: Utiliza o SQLite para armazenar os dados de forma persistente.

Tecnologias Utilizadas
Python: Linguagem de programação principal.

Streamlit: Biblioteca para criação de interfaces web de forma rápida e intuitiva.

SQLite: Banco de dados embutido, não requer um servidor separado.

Pandas: Usado para manipulação e exibição dos dados em formato de tabela.

Pré-requisitos
Certifique-se de que você tem o Python 3.7 ou superior instalado.

Como Instalar e Executar
Siga os passos abaixo para configurar e rodar a aplicação em seu ambiente local:

Clone o repositório:

Bash

git clone https://github.com/Geovani-Cp/APLICA-O-WEB-de-Cadastro-com-PYTHON-SQLite-e-STREAMLIT.git
cd APLICA-O-WEB-de-Cadastro-com-PYTHON-SQLite-e-STREAMLIT
Crie e ative um ambiente virtual (opcional, mas recomendado):

Bash

# No Windows
python -m venv venv
venv\Scripts\activate

# No macOS e Linux
python3 -m venv venv
source venv/bin/activate
Instale as dependências:

Bash

pip install -r requirements.txt
Se você não tiver o arquivo requirements.txt, pode instalar as bibliotecas manualmente com:

Bash

pip install streamlit pandas
Execute a aplicação:

Bash

streamlit run interface.py
A aplicação será iniciada e abrirá automaticamente no seu navegador padrão. Se não abrir, acesse http://localhost:8501.

Estrutura do Projeto
interface.py: Arquivo principal da aplicação Streamlit, onde a interface e a lógica de interação são definidas.

funcoes_db.py: Módulo que contém as funções para conectar ao banco de dados e executar operações (inserir, listar).

banco.db: O arquivo de banco de dados SQLite que será criado automaticamente ao rodar a aplicação pela primeira vez.
