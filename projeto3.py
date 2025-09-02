import streamlit as st

#configuração da página
st.set_page_config(
    page_title="Painel de Estudos",
    page_icon="❤️",
    layout="wide"
)

#Título
st.title("Painel de Estudos")
st.subheader("Registre e visualize seus Estudos diários")

# Barra lateral 
st.sidebar.header("Seus hábitos")
estudo = st.sidebar.slider("Horas de Estudo", 0, 6, 8)
pausas = st.sidebar.slider("Horas de pausas", 0, 5, 8)
atividades_realizadas = st.sidebar.selectbox("Atividas Realizadas",["Leitura", "Exercício", "Revisão", "nenhuma"])

#Métrias simples
st.metric("Estudo", f"{estudo} horas")
st.metric("Pausas", f"{pausas} horas")
st.metric("Exercício", atividades_realizadas)

# colunos para visualizar
col1, col2, col3 = st.columns(3)

with col1:
    st.header("Detalhe das horas estudadas")
    st.write("Você está de parabéns!" if estudo >= 8 else "Tente estudar mais")
    
with col2:
    st.header("Pausas")
    st.write("Muito bem você está se esforçando!🏋️‍♀️" if pausas >= 0 else "Você tem que se esforça mais!☹️")

with col3:
    st.header("Atividades realizadas")
    st.write("Parabéns!" if atividades_realizadas != "Nenhum" else "Tente fazer mais tarefas hoje")
#EXPANDER COM MENSAGEM EXTRA
with st.expander("Dicas rápidas"):
    st.write("- Estude pelo menos 6 horas por dia🤓")
    st.write("- Tente fazer o minímo de pausas possível😊")
    st.write("- Faça algumas atividades ao dia😉")

    #Rodapé
    st.markdown("---")
    st.markdown("Projeto com streamlit")