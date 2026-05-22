import streamlit as st
import time

# Configurando a página com título secreto e emoji
st.set_page_config(page_title="Alerta Urgente", page_icon="🚨", layout="centered")

st.title("🚨 NOTIFICAÇÃO OFICIAL DO SISTEMA 🚨")
st.write("Um relatório de auditoria interna apontou níveis críticos de saudade nas últimas horas.")

st.markdown("---")

# Pergunta interativa 1
resposta_1 = st.radio(
    "1. Quem é oficialmente a namorada mais braba de todo o estado do Rio de Janeiro?",
    ["Selecione...", "Maria Luíza (Obviamente)", "Outra opção (Gera erro no sistema)"]
)

if resposta_1 == "Maria Luíza (Obviamente)":
    st.balloons()
    st.success("🎯 Resposta correta! Você ganhou +1000 pontos de bom namorado e um vale-beijo (retirada presencial).")
    
    st.markdown("### Fase 2: O Próximo Passo")
    st.write("Agora que você provou sua idoneidade, responda com sinceridade:")
    
    # Pergunta 2
    opcao_janta = st.selectbox(
        "O que vamos jantar hoje para comemorar que é sexta-feira?",
        ["Escolha o cardápio...", "Açai", "Hamburguer", "O que você quiser, eu pago"]
    )
    
    if opcao_janta != "Escolha o cardápio...":
        st.snow() # Efeito de neve caindo
        st.markdown(f"### 🔥 ACORDO FECHADO!")
        st.write(f"O sistema registrou a opção: **{opcao_janta}**.")
        st.write("Não aceitamos cancelamentos ou estornos após a emissão deste protocolo.")
        
elif resposta_1 == "Outra opção (Gera erro no sistema)":
    st.error("❌ ERRO 404: Opção totalmente inválida. Tente novamente antes que o clima azede na sua linha do tempo.")