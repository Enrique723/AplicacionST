import streamlit as st 
import pandas as pd 
import plotly.express as px

import datetime

dfDatos = pd.read_csv("https://raw.githubusercontent.com/gcastano/datasets/main/gapminder_data.csv")

st.header("Filtrado y captura de datos")
st.write("El procesamiento de datos a travez de la ciencia de datos usuando Streamlit de python")

st.metric("Registros Totales", len (dfDatos))
st.dataframe(dfDatos, use_container_width=True)