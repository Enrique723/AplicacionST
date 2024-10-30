import json
import requests
import streamlit as st 
from streamlit_lottie import st_lottie

def get (path:str):
    with open (path, "r") as p:
        return json.load(p)
    
def get_url (url:str):
    r=requests.get(url)
    if r.status_code !=200:
        return None
    return r.json()

with st.container():
    st.subheader("Bienvenido, somos SoftIA")
    st.title("Creamos soluciones para acelrar tu negocio")
    st.write("Somos apacionados de las tecnologias y la innovacion")
    st.write("[Saber mas>](https://streamlit.io/)")
    
    with st.container():
        st.write("---")
        l_columna, r_columna = st.columns((2))
        with l_columna:
            st.header("Sobre nosotros")
            st.write("asdasdasdadasdadasdasdasdasdjskdblksahvkdjbvflkajsdbvlasjhdbcljsdbclkasdhbclsahbdclasjdkbclasdbclashdbclajshcdvljashdcjlashdbcljasdhbclashdbclsajdch sa")
            st.write("[Saber mas>](https://streamlit.io/)")

      