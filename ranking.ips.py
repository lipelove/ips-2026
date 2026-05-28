# Importação de Bibliotecas

import streamlit as st
import pandas as pd
import plotly.express as px


# Ranking IPS 2026

df = pd.DataFrame({
    "Rank": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21],

    "Município": ["Turmalina", "Veredinha", "Capelinha", "Itamarandiba", "Santa Maria do Suaçuí", "Carbonita", "Água Boa", "José Gonçalves de Minas", "Leme do Prado", "Angelândia", "Minas Novas", "Virgem da Lapa", "Berilo", "São Sebastião do Maranhão", "Jenipapo de Minas", "Chapada do Norte", "Aricanduva", "Francisco Badaró", "Setubinha", "Novo Cruzeiro", "Ladainha"],

    "Posição": ["926º", "1.342º", "1.947º", "2.216º", "2.478º", "2.677º", "3.042º", "3.073º", "3.097º", "3.165º", "3.299º", "3.349º", "3.539º", "3.644º", "4.024º", "4.279º", "4.303º", "4.842º", "5.194º", "5.307º", "5.553º"],

    "Pontuação": [64.86, 63.74, 62.29, 61.72, 61.16, 60.77, 59.98, 59.91, 59.86, 59.74, 59.45, 59.35, 58.96, 58.74, 57.90, 57.27, 57.20, 55.48, 53.73, 52.83, 47.58],

    "PIB": [23442.10, 21935.78, 26561.88, 19581.99, 17419.53, 23238.63, 18999.44, 15708.12, 16875.82, 24697.82, 17285.06, 13809.03, 14460.78, 12342.93, 14471.98, 12436.38, 17927.35, 12932.32, 13526.34, 15281.66, 11785.33],

    "Ano": [2023, 2023, 2023, 2023, 2023, 2023, 2023, 2023, 2023, 2023, 2023, 2023, 2023, 2023, 2023, 2023, 2023, 2023, 2023, 2023, 2023]
})


# Configuração da página

st.set_page_config(
    page_title="Ranking IPS 2026 - Municípios Gazeta dos Vales",
    page_icon="📊",
    layout="wide"
)

st.title("Ranking IPS 2026 - Municípios Gazeta dos Vales")

# Filtro Slider

st.subheader("Ranking Geral por Pontuação - Slider")

minimo = st.slider(
    "Pontuação mínima",
    min_value=float(df["Pontuação"].min()),
    max_value=float(df["Pontuação"].max()),
    value=float(df["Pontuação"].min())
)

filtrado = df[df["Pontuação"] >= minimo]

st.dataframe(filtrado, use_container_width=True, hide_index=True)

# Filtro Multiselect 

st.subheader("Ranking Geral por Pontuação - Multiselect")

municipios = st.multiselect(
    "Selecione os municípios",
    options=df["Município"].tolist(),
    default=["Turmalina", "Capelinha"]
)

if municipios:
    filtrado = df[df["Município"].isin(municipios)]

    st.dataframe(
        filtrado,
        use_container_width=True,
        hide_index=True
    )

    fig_multiselect = px.bar(
        filtrado,
        x="Município",
        y="Pontuação",
        text="Pontuação",
        title="Pontuação IPS 2026 dos municípios selecionados"
    )

    fig_multiselect.update_traces(
        texttemplate="%{text:.2f}",
        textposition="outside"
    )

    fig_multiselect.update_layout(
        xaxis_title="Município",
        yaxis_title="Pontuação IPS"
    )

    st.plotly_chart(fig_multiselect, use_container_width=True)

else:
    st.warning("Selecione ao menos um município.")

# Gráfico Barras

st.subheader("Ranking Geral por Pontuação - Barras")

fig_ranking = px.bar(
    df.sort_values("Pontuação", ascending=True),
    x="Pontuação",
    y="Município",
    orientation="h",
    text="Pontuação",
    title="Pontuação IPS 2026 por Município"
)

fig_ranking.update_traces(
    texttemplate="%{text:.2f}",
    textposition="outside"
)

st.plotly_chart(fig_ranking, use_container_width=True)