import streamlit as st
from pages import sobre, predicao, graficos

def main():
    st.set_page_config(page_title="Sistema de Evasão Escolar", layout="wide")

    # 🔹 Remove header e sidebar padrão do Streamlit
    st.markdown("""
        <style>
            header[data-testid="stHeader"] {
                display: none !important;
            }

            div.block-container {
                padding-top: 0rem !important;
            }

            section[data-testid="stSidebar"] {
                display: none;
            }
        </style>
    """, unsafe_allow_html=True)

    # Define a página atual
    query_params = st.query_params
    page = query_params.get("page", "sobre")
    active_page = page

    # 🔹 Estilos da Navbar
    st.markdown(f"""
        <style>
            html, body, [class*="css"] {{
                margin: 0;
                padding: 0;
                overflow-x: hidden;
            }}

            .stApp {{
                background-color: #2D6A4F;
                padding-top: 120px; /* espaço pro conteúdo não colar na navbar */
            }}

            /* NAVBAR FIXA */
            .navbar {{
                position: fixed;
                top: 0;
                left: 0;
                width: 100%;
                background-color: #1B4332;
                color: #E9F5DB;
                text-align: center;
                padding: 12px 0 15px 0;
                box-shadow: 0 2px 15px rgba(0, 0, 0, 0.3); /* sombra leve */
                z-index: 9999;
            }}

            /* TÍTULO */
            .navbar-title {{
                font-size: 26px;
                font-weight: bold;
                color: #B7E4C7;
                margin: 0;
                text-shadow: 1px 1px 2px #000;
                line-height: 1.4;
            }}

            /* CONTAINER DOS BOTÕES */
            .navbar-buttons {{
                display: flex;
                justify-content: center;
                gap: 25px;
                margin-top: 8px;
                flex-wrap: wrap;
            }}

            /* BOTÕES */
            .navbar-button {{
                background-color: #081C15;
                color: #E9F5DB;
                border: none;
                padding: 10px 25px;
                border-radius: 10px;
                cursor: pointer;
                transition: all 0.3s ease;
                font-size: 16px;
                font-weight: 500;
                box-shadow: 0 4px 10px rgba(0, 0, 0, 0.2);
            }}

            .navbar-button:hover {{
                background-color: #2D6A4F;
                color: #FFFFFF;
                transform: scale(1.05);
            }}

            /* BOTÃO ATIVO */
            .navbar-button.active {{
                background-color: #40916C !important;
                color: #FFFFFF !important;
                box-shadow: 0 0 15px #74C69D !important;
                transform: scale(1.07);
            }}
        </style>

        <!-- NAVBAR -->
        <div class="navbar">
            <div class="navbar-title">Sistema de Análise e Predição de Evasão Escolar</div>
            <div class="navbar-buttons">
                <form action="?page=sobre" method="get">
                    <button class="navbar-button {'active' if active_page == 'sobre' else ''}">Sobre</button>
                </form>
                <form action="?page=predicao" method="get">
                    <button class="navbar-button {'active' if active_page == 'predicao' else ''}">Predição</button>
                </form>
                <form action="?page=graficos" method="get">
                    <button class="navbar-button {'active' if active_page == 'graficos' else ''}">Gráficos</button>
                </form>
            </div>
        </div>
    """, unsafe_allow_html=True)

    # 🔹 Exibe a página correspondente
    if page == "sobre":
        sobre.mostrar()
    elif page == "predicao":
        predicao.mostrar()
    elif page == "graficos":
        graficos.mostrar()

if __name__ == "__main__":
    main()

















