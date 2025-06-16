import streamlit as st
import google.generativeai as genai


# Configuração da API Key e Modelo (conforme solicitado)
api_key = "AIzaSyDNAWSkFfjtNWO8UZMbSWxyY1ymdWO-fYs"
genai.configure(api_key=api_key)


# Configuração da página
st.set_page_config(page_title="Minha App", page_icon="🚀")

# Título da aplicação
st.title("Minha Primeira App Streamlit")

# Texto simples
st.write("Olá, mundo!")


# Títulos e cabeçalhos
st.title("Título Principal")
st.header("Cabeçalho")
st.subheader("Subcabeçalho")

# Texto
st.text("Texto simples")
st.write("Texto com markdown suportado")
st.markdown("**Texto em negrito** e *itálico*")

# Código
st.code("print('Hello World')", language='python')

# Entrada de texto
nome = st.text_input("Digite seu nome:")
biografia = st.text_area("Conte sobre você:")

# Números
idade = st.number_input("Idade:", min_value=0, max_value=120)
altura = st.slider("Altura (cm):", 100, 250, 170)

# Seleção
opcao = st.selectbox("Escolha uma opção:", ["A", "B", "C"])
multiplas = st.multiselect("Múltiplas escolhas:", ["X", "Y", "Z"])

# Checkbox e radio
aceito = st.checkbox("Eu aceito os termos")
genero = st.radio("Gênero:", ["Masculino", "Feminino", "Outro"])

# Botões
if st.button("Clique aqui"):
    st.write("Botão foi clicado!")

# Entrada de texto
nome = st.text_input("Digite seu nome:")
biografia = st.text_area("Conte sobre você:")

# Números
idade = st.number_input("Idade:", min_value=0, max_value=120)
altura = st.slider("Altura (cm):", 100, 250, 170)

# Seleção
opcao = st.selectbox("Escolha uma opção:", ["A", "B", "C"])
multiplas = st.multiselect("Múltiplas escolhas:", ["X", "Y", "Z"])

# Checkbox e radio
aceito = st.checkbox("Eu aceito os termos")
genero = st.radio("Gênero:", ["Masculino", "Feminino", "Outro"])

# Botões
if st.button("Clique aqui"):
    st.write("Botão foi clicado!")

# Upload de arquivo único
arquivo = st.file_uploader("Envie um arquivo", type=['csv', 'txt', 'xlsx'])

if arquivo is not None:
    # Processar arquivo CSV
    import pandas as pd
    df = pd.read_csv(arquivo)
    st.dataframe(df)

# Sidebar para controles
st.sidebar.title("Controles")
st.sidebar.write("Use os controles abaixo:")

# Widgets na sidebar
opcao = st.sidebar.selectbox("Escolha uma opção:", ["Opção 1", "Opção 2", "Opção 3"])
valor = st.sidebar.slider("Valor:", 0, 100, 50)
ativo = st.sidebar.checkbox("Ativar recurso")

# Exibir informações na sidebar
st.sidebar.info("ℹ️ Informações importantes aqui")
st.sidebar.success("✅ Operação realizada com sucesso")
st.sidebar.warning("⚠️ Atenção: verifique os dados")
st.sidebar.error("❌ Erro encontrado")


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

# Título do aplicativo
st.title("Exercício: Planejador de Roteiro de Viagem Básico com IA ✈️")
st.markdown("Descreva sua viagem ideal e deixe a IA ajudar com o planejamento!")


# Entradas do usuário
destino = st.text_input("Qual o seu destino principal?")
duracao_dias = st.number_input("Duração da viagem (em dias):", min_value=1, max_value=30, value=3, step=1)

interesses_opcoes = [
    "História e Cultura", "Natureza e Paisagens", "Gastronomia Local",
    "Praias e Relaxamento", "Aventura e Esportes", "Vida Noturna", "Compras", "Arte e Museus"
]
interesses_selecionados = st.multiselect(
    "Quais são seus principais interesses na viagem?",
    interesses_opcoes,
    default=[]
)

ritmo_viagem = st.selectbox(
    "Qual o ritmo desejado para a viagem?",
    ["Relaxado (poucas atividades por dia)", "Moderado (equilíbrio entre atividades e descanso)", "Intenso (aproveitar ao máximo cada momento)"]
)

tipo_orcamento = st.radio(
    "Qual o seu tipo de orçamento para atividades e alimentação?",
    ["Econômico (foco em opções gratuitas ou de baixo custo)", "Médio (confortável, buscando bom custo-benefício)", "Luxo (experiências premium, sem muita preocupação com gastos)"]
)

observacoes_especiais = st.text_area(
    "Observações ou pedidos especiais:",
    placeholder="Ex: viajando com crianças, prefiro transporte público, gostaria de 1 dia livre, foco em fotografia..."
)

if st.button("Gerar Sugestão de Roteiro"):
    if not destino:
        st.warning("Por favor, informe o destino da viagem.")
    elif not interesses_selecionados:
        st.warning("Por favor, selecione pelo menos um interesse para a viagem.")
    else:
        interesses_str = ", ".join(interesses_selecionados)

        prompt_aluno = (
            f"Preciso de ajuda para planejar um roteiro de viagem básico. Meu destino principal é '{destino}'.\n"
            f"A viagem terá duração de {duracao_dias} dias.\n"
            f"Meus principais interesses são: {interesses_str}.\n"
            f"O ritmo da viagem que desejo é: '{ritmo_viagem}'.\n"
            f"Meu orçamento para atividades e alimentação pode ser considerado: '{tipo_orcamento}'.\n"
            f"Observações e pedidos especiais: '{observacoes_especiais if observacoes_especiais else 'Nenhuma observação especial.'}'\n\n"
            f"Com base nessas informações, por favor, sugira um esboço de roteiro com atividades e/ou pontos turísticos. "
            f"Pode ser um resumo geral de atividades possíveis ou uma sugestão para cada dia. "
            f"Tente priorizar os interesses mencionados e adequar as sugestões ao perfil da viagem. "
            f"Gostaria de ideias práticas e, se possível, algumas dicas locais ou tipos de experiências únicas relacionadas ao destino e aos meus interesses. "
            f"Apresente a resposta de forma organizada."
        )

        st.markdown("---")
        st.markdown("⚙️ **Prompt que será enviado para a IA (para fins de aprendizado):**")
        st.text_area("",prompt_aluno, height=250)
        st.markdown("---")

        st.info("Aguarde, a IA está montando seu roteiro dos sonhos...")
        resposta_ia = gerar_resposta_gemini(prompt_aluno)

        if resposta_ia:
            st.markdown("### ✨ Sugestão de Roteiro da IA:")
            st.markdown(resposta_ia)
        else:
            st.error("Não foi possível gerar o roteiro. Verifique as mensagens acima ou tente novamente mais tarde.")