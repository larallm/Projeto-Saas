import streamlit as st
import google.generativeai as genai

api_key = "AIzaSyB1Mrx7zqfdJhEU512IYFhaAKKdF0OO7KE"
genai.configure(api_key=api_key)

try:
    # Utilizando o modelo especificado
    model = genai.GenerativeModel("gemini-2.0-flash")
except Exception as e:
    st.error(f"Erro ao carregar o modelo Gemini 'gemini-2.0-flash': {e}")
    st.info("Verifique se o nome do modelo está correto e se sua chave API tem acesso a ele.")
    st.stop()

def gerar_resposta_gemini(prompt_completo):
    try:
        response = model.generate_content(prompt_completo)

        if response.parts:
            return response.text
        else:
            if response.prompt_feedback:
                st.warning(f"O prompt foi bloqueado. Razão: {response.prompt_feedback.block_reason}")
                if response.prompt_feedback.safety_ratings:
                    for rating in response.prompt_feedback.safety_ratings:
                        st.caption(f"Categoria: {rating.category}, Probabilidade: {rating.probability}")
            return "A IA não pôde gerar uma resposta para este prompt. Verifique as mensagens acima ou tente reformular seu pedido."
    except Exception as e:
        st.error(f"Erro ao gerar resposta da IA: {str(e)}")
        if hasattr(e, 'message'): # Tenta obter mais detalhes do erro da API do Gemini
            st.error(f"Detalhe da API Gemini: {e.message}")
        return None

# Sidebar para controles
st.sidebar.title("Informações do aplicativo")
st.sidebar.write("Como usar?")

# Widgets na sidebar
ativo = st.sidebar.checkbox("Ativar recurso")

# Exibir informações na sidebar
st.sidebar.info("ℹ️ Preencha todas as informações pedidas, é importante!")
st.sidebar.success("✅ Retire suas dúvidas")
st.sidebar.warning("⚠️ Atenção: verifique se preencheu seus dados os dados")
st.sidebar.error("❌ Erro na resposta")

# Título do aplicativo
st.title("Educa Ia 📚")
st.header("Descreva sua duvida e deixe a IA ajudar com o seu estudo!")
st.subheader("Preencha o formulário a seguir para realizar sua pergunta:")



# Entradas do usuário
nome = st.text_input("Qual é o seu nome?")
idade = st.number_input("Informe a idade:", min_value=1, max_value=17, value=3, step=1)
turno = st.radio(
    "Qual período do dia é a sua aula?",
    ["Manhã", "Tarde", "Noite"]
)

turma = st.selectbox(
    "Selecione a turma:",
    ["2° ano Fundamental", "3° ano Fundamental", "4° ano",   "5° ano", "6° ano", "7° ano", "8° ano", "9° ano",
        "1° ano Ensino Médio", "2° ano Ensino Médio", "3° ano Ensino Médio"]
)

if "Fundamental" in turma:
    ano = int(turma.split("°")[0])
    if 2 <= ano <= 5:
        materias_opcoes = [
            "Língua Portuguesa", "Matemática", "Ciências", "História", "Geografia",
            "Arte", "Educação Física", "Música", "Inglês", "Teatro",
        ]
    elif 6 <= ano <= 9:
        materias_opcoes = [
            "Língua Portuguesa", "Matemática", "Ciências", "História", "Geografia",
            "Arte", "Educação Física", "Inglês", "Espanhol",
        ]
    else:
        materias_opcoes = []
elif "Ensino Médio" in turma:
    materias_opcoes = [
        "Língua Portuguesa", "Literatura", "Inglês", "História", "Geografia", "Filosofia",
        "Sociologia", "Matemática", "Física", "Química", "Biologia",
        "Artes", "Educação Física", "Espanhol", "Projeto de Vida", "Oficina de Textos"
    ]
else:
    materias_opcoes = []

materias = st.multiselect(
    "Selecione as matérias:",
    materias_opcoes
)
genero = st.radio("Gênero:", ["Masculino", "Feminino", "Outro"])

# Upload de arquivo único
arquivo = st.file_uploader("Envie sua declaração de estudante", type=['csv', 'txt', 'xlsx'])

if arquivo is not None:
    # Processar arquivo CSV
    import pandas as pd
    df = pd.read_csv(arquivo)
    st.dataframe(df)


aceito = st.checkbox("Eu aceito os termos")
if st.button("Clique aqui"):
    st.write("Você aceitou os termos!")

duvida = st.text_area(
    "Digite sua dúvida:",
    placeholder="Ex: Quantos países existem na America do Sul, como eu realizo uma equação..."
)

if st.button("Gerar um recurso para retirar duvida"):
    if not duvida:
        st.warning("Por favor, informe a  materia.")
    elif not materias:
        st.warning("Por favor, selecione pelo menos uma materia.")
    else:
        materias_str = ", ".join(materias)

        prompt_aluno = (
            f"Escreva o nome do aluno: {nome}.\n"
            f"A sua idade é {idade}.\n"
            f"Seu turno é: {turno}.\n"
            f"Sua turma é: {turma}.\n"
            f"A materia ou as materias escolhidas foram: {materias}.\n"
            f"Duvida do aluno '{duvida if duvida else 'Nenhuma dúvida inserida.'}'\n\n"
            f"Faça uma saudação ao usuário "
            f"Com base nessas informações, por favor, dê uma explicação ao usuário "
            f"Pode ser um resumo geral da duvida. "
            f"Dê dicas de como o aluno pode estudar com base no turno dele. "
            f"Gostaria de uma forma clara para explicar o estudante com base na idade dele sobre o assunto. "
            f"Apresente a resposta de forma organizada."
        )

        st.markdown("---")
        st.markdown("⚙️ **Prompt que será enviado para a IA (para fins de aprendizado):**")
        st.text_area("",prompt_aluno, height=250)
        st.markdown("---")

        st.info("Aguarde, a IA está encntrando a melhor explicação para você...")
        resposta_ia = gerar_resposta_gemini(prompt_aluno)

        if resposta_ia:
            st.markdown("### ✨ Retirando a dúvida:")
            st.markdown(resposta_ia)
        else:
            st.error("Não foi possível explicar. Verifique as mensagens acima ou tente novamente mais tarde.")