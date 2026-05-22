import streamlit as st

# Configurando a página
st.set_page_config(page_title="Relatório de Auditoria", page_icon="🚨", layout="centered")

# Criando a memória do site (Session State) para o jogo funcionar por etapas
if 'fase' not in st.session_state:
    st.session_state.fase = 1
if 'janta' not in st.session_state:
    st.session_state.janta = ""

# --- FASE 1: PERGUNTA DA NAMORADA ---
if st.session_state.fase == 1:
    st.title("🚨 NOTIFICAÇÃO OFICIAL DE AUDITORIA 🚨")
    st.write("O sistema detectou níveis críticos de saudade nas últimas horas.")
    st.markdown("---")
    
    resposta_1 = st.radio(
        "1. Quem é oficialmente a namorada mais braba de todo o estado do Rio de Janeiro?",
        ["Selecione...", "Maria Luíza (Obviamente)", "Outra opção"]
    )
    
    if resposta_1 == "Maria Luíza (Obviamente)":
        st.balloons() # Balões na hora do acerto
        st.session_state.fase = 2
        st.rerun()
        
    elif resposta_1 == "Outra opção":
        st.error("❌ ERRO 404: Opção totalmente inválida. Tente novamente.")

# --- FASE 2: ESCOLHA DA JANTA ---
elif st.session_state.fase == 2:
    st.title("⏳ FASE 2: CONFIGURAÇÃO DO PROTOCOLO")
    st.write("Identidade confirmada com sucesso. Agora, defina os parâmetros da janta:")
    st.markdown("---")
    
    opcao_janta = st.selectbox(
        "O que vamos jantar hoje para comemorar que é sexta-feira?",
        ["Escolha o cardápio...", "Açai", "Hambúrguer", "O que você quiser, eu pago, minha deusa"]
    )
    
    if opcao_janta != "Escolha o cardápio...":
        st.snow() # Neve na hora de fechar a janta
        st.session_state.janta = opcao_janta
        st.session_state.fase = 3
        st.rerun()

# --- FASE 3: O ACORDO ---
elif st.session_state.fase == 3:
    st.title("🔥 PROTOCOLO EMITIDO COM SUCESSO!")
    st.write(f"O sistema registrou a janta: **{st.session_state.janta}**.")
    st.write("Não aceitamos cancelamentos ou estornos após a emissão deste documento.")
    st.markdown("---")
    
    if st.button("CLIQUE AQUI PARA VALIDAR O CERTIFICADO FINAL"):
        st.session_state.fase = 4
        st.rerun()

# --- FASE 4: O GRAN FINALE (O Alvo Principal) ---
elif st.session_state.fase == 4:
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: center; font-size: 70px;'>❤️❤️❤️❤️</h1>", unsafe_allow_html=True)
    
    # Mensagem principal estourando na tela
    st.markdown("<h1 style='text-align: center; color: #ff4b4b; font-size: 45px; font-weight: bold;'>YURI, VOCÊ É UM GOSTOSO!</h1>", unsafe_allow_html=True)
    
    st.markdown("<h1 style='text-align: center; font-size: 70px;'>❤️❤️❤️❤️</h1>", unsafe_allow_html=True)
    
    # Fechamento fofo completo
    st.markdown("<p style='text-align: center; font-size: 26px; font-weight: bold; color: #333;'>Te amo!</p>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-size: 22px; color: #555;'>Vejo você mais tarde. 🥰</p>", unsafe_allow_html=True)
    
    # Botão discreto na lateral caso queira testar de novo
    if st.sidebar.button("Reiniciar Sistema 🔄"):
        st.session_state.fase = 1
        st.session_state.janta = ""
        st.rerun()
