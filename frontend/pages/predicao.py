import streamlit as st
import requests

def mostrar():
    st.markdown('<div class="subtitulo">Predição</div>', unsafe_allow_html=True)

    col1, col2 = st.columns([1, 2], gap="large")

    with col1:
        # ======= MAPAS DE OPÇÕES (TEXTO → VALOR NUMÉRICO) =======
        educacao_opcoes = {
            "Nenhuma": 0,
            "Primário": 1,
            "Fundamental": 2,
            "Médio": 3,
            "Superior": 4
        }

        tempo_estudo_opcoes = {
            "Muito baixo": 0,
            "Baixo": 1,
            "Médio": 2,
            "Alto": 3,
            "Muito alto": 4
        }

        tempo_viagem_opcoes = {
            "Curto": 0,
            "Moderado": 1,
            "Longo": 2,
            "Muito longo": 3,
            "Extenso": 4
        }

        tempo_livre_opcoes = {
            "Muito baixo": 0,
            "Baixo": 1,
            "Médio": 2,
            "Alto": 3,
            "Muito alto": 4
        }

        saidas_opcoes = {
            "Nunca": 0,
            "Raramente": 1,
            "Às vezes": 2,
            "Frequentemente": 3,
            "Sempre": 4
        }

        alcool_opcoes = {
            "Nunca": 0,
            "Raramente": 1,
            "Às vezes": 2,
            "Frequentemente": 3,
            "Sempre": 4
        }

        # ======= CAMPOS DE ENTRADA =======
        Age = st.number_input("Idade", min_value=10, max_value=25)
        Gender = st.selectbox("Gênero", ["M", "F"])
        Address = st.selectbox("Endereço", ["U (Urbano)", "R (Rural)"])
        Mother_Education = educacao_opcoes[st.selectbox("Escolaridade da Mãe", list(educacao_opcoes.keys()))]
        Father_Education = educacao_opcoes[st.selectbox("Escolaridade do Pai", list(educacao_opcoes.keys()))]
        Mother_Job = st.text_input("Profissão da Mãe")
        Travel_Time = tempo_viagem_opcoes[st.selectbox("Tempo de Viagem", list(tempo_viagem_opcoes.keys()))]
        Study_Time = tempo_estudo_opcoes[st.selectbox("Tempo de Estudo", list(tempo_estudo_opcoes.keys()))]
        Free_Time = tempo_livre_opcoes[st.selectbox("Tempo Livre", list(tempo_livre_opcoes.keys()))]
        Going_Out = saidas_opcoes[st.selectbox("Frequência de Sair", list(saidas_opcoes.keys()))]
        Weekend_Alcohol_Consumption = alcool_opcoes[st.selectbox("Consumo de Álcool no Fim de Semana", list(alcool_opcoes.keys()))]
        Weekday_Alcohol_Consumption = alcool_opcoes[st.selectbox("Consumo de Álcool Durante a Semana", list(alcool_opcoes.keys()))]
        Number_of_Absences = st.number_input("Número de Faltas", 0, 100)
        Grade_1 = st.number_input("Nota 1º Período", 0, 20)
        Grade_2 = st.number_input("Nota 2º Período", 0, 20)
        Final_Grade = st.number_input("Nota Final", 0, 20)
        Wants_Higher_Education = st.selectbox("Deseja Ensino Superior?", ["Sim", "Não"])
        Internet_Access = st.selectbox("Acesso à Internet", ["Sim", "Não"])
        In_Relationship = st.selectbox("Em Relacionamento?", ["Sim", "Não"])

        if st.button("VERIFICAR RISCO DE EVASÃO", key="predict_button"):
            data = {
                "Age": Age,
                "Gender": Gender,
                "Address": Address.split()[0],
                "Mother_Education": Mother_Education,
                "Father_Education": Father_Education,
                "Mother_Job": Mother_Job,
                "Travel_Time": Travel_Time,
                "Study_Time": Study_Time,
                "Free_Time": Free_Time,
                "Going_Out": Going_Out,
                "Weekend_Alcohol_Consumption": Weekend_Alcohol_Consumption,
                "Weekday_Alcohol_Consumption": Weekday_Alcohol_Consumption,
                "Number_of_Absences": Number_of_Absences,
                "Grade_1": Grade_1,
                "Grade_2": Grade_2,
                "Final_Grade": Final_Grade,
                "Wants_Higher_Education": Wants_Higher_Education,
                "Internet_Access": Internet_Access,
                "In_Relationship": In_Relationship
            }

            try:
                response = requests.post("http://127.0.0.1:8000/predict", json=data)
                if response.status_code == 200:
                    result = response.json()
                    st.session_state["resultado"] = result.get("mensagem", "Erro ao interpretar resposta")
                else:
                    st.error(f"Erro {response.status_code}: {response.text}")
            except Exception as e:
                st.error(f"Erro ao conectar com o servidor: {e}")

    with col2:
        st.markdown('<div class="subtitulo">Resultado</div>', unsafe_allow_html=True)
        resultado = st.session_state.get("resultado", "O RISCO DESSE ALUNO EVADIR É :")
        st.markdown(f'<div class="resultado">{resultado}</div>', unsafe_allow_html=True)
