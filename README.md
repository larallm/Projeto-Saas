<h1 align="center">Educa IA 📚 - Aplicativo de tirar dúvida e apredizagem educacional </h1>

## O Educa Ia tem o intuito de facilitar a aprendizagem dos estudates,ao retirar dúvidas e dar dicas de como estudar melhor a partir do seu horário de aula e idade.

# Clone o Repositório:
* https://github.com/larallm/Projeto-Saas.git

# Instalação:Criando um ambiente virtual (venv)

## Windows:
###  Criar ambiente virtual:
* python -m venv streamlit_env
### Ativar ambiente virtual:
* streamlit_env\Scripts\activate
### Desativar:
* deactivate


## Mac/Linux:
###  Criar ambiente virtual:
* python3 -m venv streamlit_env
### Ativar ambiente virtual:
* source streamlit_env/bin/activate
### Desativar:
* deactivate

# Verificando se o ambiente está ativo:
* (streamlit_env) C:\seu_projeto>


# Instalação das bibliotecas:
* Obs - é necessário que o ambiente virtual esteja inicializado para realizar a instalação das bibliotecas

## Windows/Linux:
* pip list
* pip install streamlit
* pip install google.generativeai
* pip freeze > requirements.txt
* pip install python-dotenv

## Mac:
* pip3 list
* pip3 install streamlit
* pip3 install google.generativeai
* pip3 freeze > requirements.txt
* pip3 install python-dotenv


# Verificação da instalação
* streamlit hello

# Executando uma aplicação
* streamlit run main.py
  
# Crie uma chave API do Google Gemini
* https://aistudio.google.com/app/apikey?hl=pt-br
## Esconda sua chave:
* Crie um file . env
* Escreva sua chave nela

# Uso:
* Ao preencher o formúlario, a IA irá gerar uma solução ao seu problema,  de acordo com a sua idade, turno e matéria selecionada, além de dicas de estudo.

###  Passos:
* Preencha seu nome, idade e turno.
* Selecione a sua turma escolar.
* Escolha uma ou mais matérias relacionadas à sua dúvida.
* (Opcional) Envie uma declaração de estudante (.csv, .txt, ou .xlsx).
* Digite sua dúvida no campo apropriado.
* Clique em "Gerar um recurso para retirar dúvida".

# Créditos:
### Desenvolvido por Lara Lopes Marques e Lucas Kaiky Pessoa.

# Streamlit:
### https://projeto-saas-cuqcnnquf2bmz8sbvmsfzs.streamlit.app


