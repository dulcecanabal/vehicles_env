import pandas as pd
import plotly.express as px
import streamlit as st

# Cargar los datos
car_data = pd.read_csv('vehicles_us.csv')

# Encabezado principal 
st.header('Análisis de datos de vehículos')

# Crear un botón para el histograma
build_histogram = st.checkbox('Construir un histograma')

if build_histogram:  # al hacer clic en la casilla de verificación
    # Escribir un mensaje
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    
    # Crea el histograma
    fig = px.histogram(car_data, x="odometer")
    
    # Muestra un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

# Crear una casilla de verificación para el gráfico de dispersión
build_scatter = st.checkbox('Construir un gráfico de dispersión')

if build_scatter:  # al hacer clic en la casilla
    st.write('Creación de un gráfico de dispersión (odometer vs price)')
    
    # Crea el gráfico de dispersión
    fig_scatter = px.scatter(car_data, x="odometer", y="price")
    
    # Muestra el gráfico interactivo
    st.plotly_chart(fig_scatter, use_container_width=True)
