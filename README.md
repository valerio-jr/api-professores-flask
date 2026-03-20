🍎 API de Gerenciamento de Professores (CRUD)
Esta é uma API REST desenvolvida em Python com o framework Flask para a gestão de um cadastro de professores. O projeto utiliza um arquivo JSON para persistência de dados, garantindo que as informações sejam mantidas mesmo após o encerramento da aplicação.

🚀 Tecnologias Utilizadas
Python 3

Flask (Framework Web)

JSON (Base de dados local)

🛠️ Como Executar a Aplicação
Clone o repositório:

Bash
git clone https://github.com/valerio-jr/atividades-disciplina-PROGRAMA-O-PARA-WEB-I.git
Instale a dependência necessária (Flask):

Bash
pip install flask
Inicie o servidor:

Bash
python app.py
A API estará rodando em: http://127.0.0.1:5000

📑 Documentação das Rotas (Coleção de Endpoints)
Abaixo estão listados todos os endpoints disponíveis na API para a manipulação dos dados de professores. Esta seção serve como a documentação oficial das rotas do projeto.

Método	Rota	Descrição	Exemplo de JSON (Corpo da Requisição)

GET	/professores	Retorna a lista completa de todos os professores cadastrados.	N/A
GET	/professores/<id>	Consulta e retorna os detalhes de um professor específico pelo seu ID.	N/A
POST	/professores	Cadastra um novo professor no sistema. Requer nome, email e disciplina.	{"nome": "Fulano", "email": "fulano@email.com", "disciplina": "Web"}
PUT	/professores/<id>	Atualiza os dados de um professor já existente no sistema.	{"nome": "Nome Atualizado"}
DELETE	/professores/<id>	Remove permanentemente um professor do banco de dados (JSON).	N/A

📂 Estrutura do Projeto
app.py: Código fonte contendo a lógica das rotas, tratamento de erros e manipulação do JSON.

professores.json: Arquivo utilizado como banco de dados persistente (armazenamento local).

.gitignore: Arquivo de configuração para ignorar pastas temporárias como venv e __pycache__.

README.md: Documentação completa com instruções de uso e guia da API.
