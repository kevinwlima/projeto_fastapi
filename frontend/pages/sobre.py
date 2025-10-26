import streamlit as st

def mostrar():
    st.markdown("""
        <style>
            .stApp {
                background-color: #2D6A4F;
            }

            /* Centraliza apenas o card, sem afetar o cabeçalho */
            .sobre-container {
                display: flex;
                justify-content: center;
                align-items: center;
                height: 80vh; /* controla a altura da área central */
                margin-top: 50px; /* espaço abaixo do título */
            }

            /* Card principal */
            .sobre-card {
                background-color: #1B4332;
                color: #E9F5DB;
                border-radius: 20px;
                box-shadow: 0 8px 30px rgba(0,0,0,0.5);
                padding: 45px 60px;
                width: 85%;
                max-width: 950px;
                line-height: 1.8;
                font-size: 18px;
                text-align: justify;
                animation: fadeIn 0.8s ease-in-out;
            }

            /* Título dentro do card */
            .sobre-titulo {
                text-align: center;
                color: #B7E4C7;
                font-size: 30px;
                font-weight: bold;
                margin-bottom: 25px;
            }

            .sobre-texto {
                color: #D8F3DC;
                margin-bottom: 18px;
            }

            .sobre-texto b {
                color: #FFFFFF;
            }

            .emoji {
                font-size: 22px;
            }

            @keyframes fadeIn {
                from {opacity: 0; transform: translateY(10px);}
                to {opacity: 1; transform: translateY(0);}
            }
        </style>

        <div class="sobre-container">
            <div class="sobre-card">
                <div class="sobre-titulo">📘 Sobre o Sistema</div>
                <div class="sobre-texto">
                    Este sistema tem como objetivo prever a probabilidade de evasão escolar com base em fatores
                    socioeconômicos, familiares e de desempenho do aluno.
                </div>
                <div class="sobre-texto">
                    Com base nos dados inseridos, o modelo de aprendizado de máquina analisa os principais
                    indicadores que contribuem para o risco de evasão, oferecendo aos gestores escolares uma
                    ferramenta de apoio à tomada de decisão.
                </div>
                <div class="sobre-texto">
                    Desenvolvido com <b>FastAPI</b> no backend e <b>Streamlit</b> no frontend, o sistema busca
                    unir performance, acessibilidade e facilidade de uso.
                </div>
        </div>
    """, unsafe_allow_html=True)
