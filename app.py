import streamlit as st
import pandas as pd
import plotly_express as px

st.header('Análise de Dados de Veículos - Dashboard Interativo')

car_data = pd.read_csv('vehicles.csv') 

build_histogram = st.checkbox('Criar um histograma')
build_scatter = st.checkbox('Criar um gráfico de dispersão')

if build_histogram:
    st.write('Exibindo distribuição da quilometragem (odômetro):')
    
    fig_hist = px.histogram(car_data, x="odometer")
    
    st.plotly_chart(fig_hist, use_container_width=True)

if build_scatter:
    st.write('Exibindo relação entre quilometragem e preço:')
    
    fig_scatter = px.scatter(car_data, x="odometer", y="price")
    
    st.plotly_chart(fig_scatter, use_container_width=True)