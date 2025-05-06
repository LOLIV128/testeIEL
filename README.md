Este projeto foi desenvolvido como parte de um desafio técnico. Ele consiste em:

- Criar um banco de dados SQLite chamado `company.db` com uma tabela `workers`.
- Realizar consultas SQL diretamente no banco (sem uso de pandas).
- Exibir os dados de forma visual através de uma interface web com Django (HTML).

📁 Estrutura do Projeto

testeIEL\_testeIEL/
│
├── workers/                # App Django com os modelos e views
│   └── ...
│   ├── templates/
│       └── dashboard.html      # Interface HTML com os dados consultados
├── company.db              # Banco de dados SQLite (incluso no repositório)
├── manage.py
├── requirements.txt
└── README.md

🧱 Tabela do Banco de Dados

A tabela `workers` foi criada no banco `company.db` com os seguintes campos:

- `nome` (texto)
- `idade` (inteiro)
- `cargo` (texto)
- `salario` (float)

Os dados foram inseridos diretamente via código SQL no início do projeto.

🔍 Consultas Realizadas

As consultas SQL são feitas diretamente usando `sqlite3` no Django, sem bibliotecas como pandas. Entre as consultas, temos:

- Lista de cargos distintos
- Quantidade de funcionários por cargo
- Top 5 maiores e menores salários
- Média salarial por cargo
- Funcionário com maior salário em cada cargo

💻 Interface Web

A interface foi construída com HTML e Django. Os dados são renderizados em `dashboard.html`.

Para visualizar a interface:

bash
python manage.py runserver


Depois, acesse: http://127.0.0.1:8000/

✅ Como Executar o Projeto

1. Clone o repositório:

2. Crie um ambiente virtual e ative-o(opcional): 

  bash
  python -m venv venv
  source venv/bin/activate  # No Windows: venv\Scripts\activate
  
3. Instale as dependências:

  bash
  pip install -r requirements.txt
 

4. Execute o servidor Django:

  bash
  python manage.py runserver
 

⚙️ Tecnologias Utilizadas

* Python
* Django
* SQLite
* HTML/CSS

📄 Licença

Este projeto foi feito para fins educacionais e como parte de um teste técnico.

