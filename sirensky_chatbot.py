import streamlit as st

# Configuração da página
st.set_page_config(
    page_title="SirenSky EcoBot",
    page_icon="🌊",
    layout="centered"
)

# Estilização personalizada (letras mais claras e visíveis)
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg, #071925 0%, #0d2b3e 50%, #093532 100%);
        color: #ffffff !important;
    }
    p, span, label, div {
        color: #f8fafc !important;
    }
    .stButton > button {
        width: 100%;
        border-radius: 20px;
        border: 1px solid #38bdf8;
        background-color: rgba(14, 165, 233, 0.2);
        color: #ffffff !important;
        font-weight: 600;
        padding: 10px 15px;
        text-align: left;
        transition: all 0.2s ease;
    }
    .stButton > button:hover {
        background-color: #0284c7;
        color: white;
        border-color: #7dd3fc;
    }
    </style>
""", unsafe_allow_html=True)

# Base de conhecimento com as perguntas e respostas
PERGUNTAS_RESPOSTAS = {
    "♻️ Como separar lixo para reciclagem?": (
        "**Passo a passo para separar corretamente:**\n\n"
        "1. **Separe seco do úmido:** Divida entre recicláveis (papel, plástico, vidro, metal) e orgânicos/rejeitos.\n"
        "2. **Higienize as embalagens:** Passe uma água rápida ou guardanapo usado em potes de iogurte e latas para evitar mau cheiro e pragas.\n"
        "3. **Não amasse papéis em excesso:** Caixas de papelão devem ser desmontadas para ocupar menos espaço.\n"
        "4. **Cuidado com vidros:** Embrulhe cacos em jornal ou coloque dentro de garrafas PET cortadas para proteger os coletores.\n"
        "5. **Descarte especial:** Pilhas, baterias, eletrônicos e óleo de cozinha vão para pontos de entrega voluntária (PEVs)."
    ),
    "🔄 O que é economia circular?": (
        "A **economia circular** é um modelo de produção e consumo que substitui o modelo linear tradicional (*extrair → produzir → descartar*).\n\n"
        "Nela, os materiais e produtos são mantidos em uso pelo maior tempo possível por meio de:\n"
        "- **Reutilização e reparo** de objetos;\n"
        "- **Remanufatura** de peças;\n"
        "- **Reciclagem** eficiente para que o resíduo vire matéria-prima novamente;\n"
        "- **Design sustentável**, pensado desde o início para não gerar lixo."
    ),
    "🐢 Como o plástico afeta os oceanos?": (
        "Milhões de toneladas de plástico chegam aos oceanos todos os anos, causando impactos graves:\n\n"
        "- **Ingestão e sufocamento:** Tartarugas, aves marinhas e peixes confundem sacolas e tampinhas com alimento.\n"
        "- **Microplásticos:** O sol e as ondas fragmentam o plástico em partículas invisíveis que entram na cadeia alimentar (chegando até nós).\n"
        "- **Destruição de habitats:** Redes fantasma e resíduos sufocam recifes de coral e manguezais.\n"
        "- **Alteração química:** Plásticos liberam toxinas na água à medida que se degradam."
    ),
    "🥽 O que é SirenVR?": (
        "O **SirenVR** é a experiência de **Realidade Virtual** do ecossistema SirenSky voltada para educação ambiental imersiva.\n\n"
        "Com óculos de VR, estudantes e visitantes mergulham virtualmente nos oceanos para explorar ecossistemas marinhos, visualizar de perto o impacto da poluição plástica e compreender como nossas atitudes em terra protegem a vida marinha."
    ),
    "🏫 Como o SirenSTEAM atua nas escolas?": (
        "O **SirenSTEAM** integra **Ciência, Tecnologia, Engenharia, Artes e Matemática (STEAM)** à educação climática e oceânica nas escolas.\n\n"
        "A atuação acontece por meio de:\n"
        "- **Oficinas práticas e projetos mão na massa** focados em sustentabilidade;\n"
        "- **Uso de tecnologia imersiva** (como o SirenVR) em sala de aula;\n"
        "- **Desafios de inovação**, incentivando alunos a criarem soluções reais para problemas ambientais da própria comunidade."
    ),
    "🌱 Dicas para uma vida mais sustentável": (
        "Pequenas mudanças diárias geram grande impacto ao longo do tempo:\n\n"
        "- **Adote retornáveis:** Tenha sempre sua garrafa de água, ecobag e copo reutilizável.\n"
        "- **Reduza o plástico de uso único:** Evite canudos, talheres e embalagens descartáveis desnecessárias.\n"
        "- **Consuma de forma consciente:** Compre apenas o necessário e priorize produtores locais.\n"
        "- **Economize recursos:** Feche a torneira ao escovar os dentes, reduza o tempo no banho e apague luzes de ambientes vazios.\n"
        "- **Composte orgânicos:** Transforme restos de frutas e legumes em adubo para plantas."
    )
}

# Cabeçalho do Chatbot
st.title("🌊 SirenSky EcoBot")
st.caption("Seu guia interativo sobre sustentabilidade, oceanos e inovação ambiental.")
st.divider()

# Inicializa o histórico da conversa
if "mensagens" not in st.session_state:
    st.session_state.mensagens = [
        {
            "role": "assistant",
            "content": "Olá! Bem-vindo ao **SirenSky**. Clique em uma das perguntas abaixo ou digite sua dúvida sobre sustentabilidade e nossos projetos:"
        }
    ]

# Função para processar pergunta e gerar resposta
def responder(pergunta_usuario):
    st.session_state.mensagens.append({"role": "user", "content": pergunta_usuario})
    
    resposta = PERGUNTAS_RESPOSTAS.get(pergunta_usuario)
    
    if not resposta:
        texto = pergunta_usuario.lower()
        if "lixo" in texto or "recicla" in texto or "separar" in texto:
            resposta = PERGUNTAS_RESPOSTAS["♻️ Como separar lixo para reciclagem?"]
        elif "circular" in texto or "economia" in texto:
            resposta = PERGUNTAS_RESPOSTAS["🔄 O que é economia circular?"]
        elif "plástico" in texto or "plastico" in texto or "oceano" in texto:
            resposta = PERGUNTAS_RESPOSTAS["🐢 Como o plástico afeta os oceanos?"]
        elif "vr" in texto or "virtual" in texto or "sirenvr" in texto:
            resposta = PERGUNTAS_RESPOSTAS["🥽 O que é SirenVR?"]
        elif "steam" in texto or "escola" in texto:
            resposta = PERGUNTAS_RESPOSTAS["🏫 Como o SirenSTEAM atua nas escolas?"]
        elif "dica" in texto or "sustentavel" in texto or "sustentável" in texto:
            resposta = PERGUNTAS_RESPOSTAS["🌱 Dicas para uma vida mais sustentável"]
        else:
            resposta = (
                "Ainda estou aprendendo sobre esse assunto! 🌱\n\n"
                "Experimente clicar em um dos **botões de perguntas rápidas** abaixo para saber mais sobre reciclagem, economia circular, oceanos, **SirenVR** e **SirenSTEAM**."
            )
            
    st.session_state.mensagens.append({"role": "assistant", "content": resposta})

# Exibe o histórico de mensagens na tela
for msg in st.session_state.mensagens:
    avatar = "🌊" if msg["role"] == "assistant" else "🧑‍💻"
    with st.chat_message(msg["role"], avatar=avatar):
        st.markdown(msg["content"])

st.markdown("#### 💡 Perguntas rápidas:")

# Cria grade de 2 colunas com os 6 botões
perguntas_lista = list(PERGUNTAS_RESPOSTAS.keys())
col1, col2 = st.columns(2)

for i, pergunta in enumerate(perguntas_lista):
    coluna_atual = col1 if i % 2 == 0 else col2
    with coluna_atual:
        if st.button(pergunta, key=f"btn_{i}"):
            responder(pergunta)
            st.rerun()

# Campo opcional para o usuário também poder digitar
if prompt := st.chat_input("Digite uma pergunta sobre o SirenSky ou sustentabilidade..."):
    responder(prompt)
    st.rerun()