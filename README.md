Recomendador de Cursos

Este projeto é um recomendador de cursos que utiliza Python (Flask) no backend e Prolog para a lógica de recomendação.

Requisitos

Python 3.x

SWI-Prolog

Navegador moderno

Pip packages: flask

Como executar

Instale as dependências do Python:

pip install flask


Certifique-se de ter o SWI-Prolog instalado e disponível no PATH.

Execute o backend Flask:

python app.py


Abra o navegador e acesse:

http://localhost:5000


Digite o nome de um aluno (ex.: joao, maria, pedro) e veja as recomendações de cursos.

Estrutura do projeto
projeto_recomendador/
├── app.py          # Backend em Flask
├── kb.pl           # Base de conhecimento Prolog
├── templates/
│   └── index.html  # Página principal
└── static/
    ├── app.js      # JavaScript
    └── styles.css  # CSS
