import streamlit as st
import matplotlib.pyplot as plt

def mostrar():
    st.markdown('<div class="subtitulo">Análise Gráfica</div>', unsafe_allow_html=True)

    st.write("Aqui você pode visualizar estatísticas relacionadas à evasão escolar.")

    # Exemplo de gráfico de pizza
    dados = {"Baixo Risco": 45, "Médio Risco": 30, "Alto Risco": 25}
    fig, ax = plt.subplots()
    ax.pie(dados.values(), labels=dados.keys(), autopct="%1.1f%%", startangle=90)
    ax.set_title("Distribuição do Risco de Evasão")
    st.pyplot(fig)

    # Exemplo de gráfico de barras
    st.write("Distribuição por Escolaridade dos Pais:")
    categorias = ["Nenhuma", "Primário", "Fundamental", "Médio", "Superior"]
    valores = [10, 20, 25, 30, 15]
    fig2, ax2 = plt.subplots()
    ax2.bar(categorias, valores, color="#1B4332")
    ax2.set_xlabel("Escolaridade")
    ax2.set_ylabel("Quantidade de Alunos")
    ax2.set_title("Escolaridade dos Pais e Evasão")
    st.pyplot(fig2)
