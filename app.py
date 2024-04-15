# importando as bibliotecas
import streamlit as st
import pandas as pd
import plotly.express as px
import os

print(os.listdir('notebooks'))

car_data = pd.read_csv('../notebooks/vehicles.csv')  # lendo os dados

st.header('Análise de anúncios de vendas de carros')  # cabeçalho


# Caixa de seleção para escolher o tipo de gráfico
build_histogram = st.checkbox('Criar um histograma')
build_scatterplot = st.checkbox('Criar um gráfico de dispersão')

# Se a caixa de seleção para histograma estiver selecionada
if build_histogram:
    # Escrever mensagem
    st.write('Criando um histograma para a coluna odometer')

    # Criar histograma
    fig = px.histogram(car_data, x="odometer")

    # Exibir o gráfico Plotly interativo
    st.plotly_chart(fig, use_container_width=True)

# Se a caixa de seleção para gráfico de dispersão estiver selecionada
if build_scatterplot:
    # Escrever mensagem
    st.write(
        'Criando um gráfico de dispersão para as colunas odometer e price')

    # Criar gráfico de dispersão
    fig = px.scatter(car_data, x='odometer', y='price')

    # Exibir o gráfico Plotly interativo
    st.plotly_chart(fig, use_container_width=True)
