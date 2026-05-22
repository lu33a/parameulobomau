import streamlit as st
import time

st.set_page_config(page_title="Relatório de Auditoria", page_icon="🚨", layout="centered")

# --- TRUQUE NINJA PARA OS CORAÇÕES ---
def coracoes():
    # Isso aqui é um pequeno código em CSS que faz os corações "choverem" na tela
    st.markdown("""
        <style>
        .heart { color: red; font-size: 30px; position: fixed; top: -10%; z-index: 9999; animation: fall 3s linear forwards; }
        @keyframes fall { to { top: 110%; transform: rotate(360deg); } }
        </style>
        <div class="heart" style="left:10%">❤️</div><div class="heart" style="left:30%">❤️</div>
        <div class="heart" style="left:50%">❤️</div><div class="heart" style="left:70%">❤️</div>
        <div class="heart" style="left:90%">❤️</div>
    """, unsafe_allow_html=True)

st.title("🚨 NOTIFICAÇÃO OFICIAL DO SISTEMA 🚨")
st.write("Auditoria de saudade nível crítico detectada.")

st.markdown("---")

resposta_1 = st.radio(
    "1. Quem é a namorada mais braba do RJ?",
    ["Selecione...", "Maria Luíza", "Outra opção"]
)

if resposta_1 == "Maria Luíza":
    st.balloons()
    st.success("🎯 Resposta correta!")
    
    opcao_janta = st.selectbox(
        "O que vamos jantar hoje?",
        ["Escolha...", "Açai", "Hamburguer", "O que você quiser eu pago, minha deusa!"]
    )
    
    if opcao_janta != "Escolha...":
        st.snow()
        st.markdown("### 🔥 ACORDO FECHADO!")
        st.write(f"Protocolo registrado: **{opcao_janta}**.")
        
        # --- O GRAN FINALE ---
        st.markdown("---")
        if st.button("CLIQUE AQUI PARA ENCERRAR O PROTOCOLO"):
            coracoes() # Chama a função dos corações
            st.header("💖 Yuri, você é um gostoso! 💖")
            st.write("Te amo! Vejo você mais tarde. 🥰")
