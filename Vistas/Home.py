import streamlit as st
from streamlit_lottie import st_lottie
import json
import requests

def get(path: str):
    with open(path, "r") as p:
        return json.load(p)

# Inicio de página
with st.container():
    st.subheader("Bienvenidos, Somos softia")
    st.title("Creamos soluciones para acelerar tu negocio")
    st.write(
        "Somos unos apasionados de las tecnologías y la innovación, especializados en el sector de la digitalización y automatización de negocios. Nos gusta crear soluciones para resolver problemas y mejorar procesos."
    )
    st.write("[Saber más >](https://share.streamlit.io/user/diether28)")

# Sobre nosotros
with st.container():
    st.write("---")
    texto_columna, imagen_columna = st.columns((1, 2))
    with texto_columna:
        st.subheader("Sobre nosotros")
        st.write(
            """
            Nuestro objetivo es aportar valor a los negocios, ayudándoles a ahorrar tiempo y dinero a través de la implantación de nuevas tecnologías como la inteligencia artificial, análisis de datos o implantación de software de automatización.

            Seguramente te vamos a poder ayudar si:
            
            - Tienes un negocio y quieres mejorar tus procesos de trabajo para ahorrar tiempo y dinero.
            - Tienes trabajadores que emplean parte de su jornada en realizar tareas repetitivas sin valor añadido para tu negocio.
            - No tienes claras las métricas de tu negocio y quieres tomar decisiones basadas en datos.
            - Quieres mejorar la experiencia de tus clientes.
            - Usas herramientas de software antiguas o poco eficientes o procesos en los que usas papel y bolígrafo.

            ***Si esto suena interesante para ti puedes contactarnos a través del formulario que encontrarás al final de la página.***
            """
        )
    with imagen_columna:
        path = get("animacion/ani.json")
        st_lottie(path, key="about_animation")

# Servicios
with st.container():
    st.write("---")
    st.header("Servicios")
    texto_columna, imagen_columna = st.columns((1, 2))
    with texto_columna:
        st.subheader("Diseño de aplicaciones")
        st.write(
            """
            Si en tus procesos diarios tienes que introducir información en diferentes fuentes de datos o bien tienes que 
            trabajar con documentación en papel, es hora de pensar en implementar una aplicación en tu negocio para potenciar y optimizar el funcionamiento de los procesos diarios.
            """
        )
        st.write("[Ver servicios >](https://share.streamlit.io/user/diether28)")
    with imagen_columna:
        path = get("animacion/ani.json")
        st_lottie(path, key="services_animation")

# Contactos
st.subheader("Contactos")

form = st.form(key="home", clear_on_submit=True)
with form:
    input_nombre = st.text_input("Nombre:", placeholder="Escriba su nombre")
    input_correo = st.text_input("Correo electrónico", placeholder="Escriba su correo electrónico")
    input_area = st.text_area("Comentario")
    button_submit = form.form_submit_button("Enviar")

# Footer
with st.container():
    st.write("---")
    p1, p2, p3 = st.columns(3)
    with p1:
        st.subheader("Contactos:")
        st.write("***Dirección:*** Juigalpa, Chontales-Nicaragua")
        st.write("***Teléfono:*** +(505)0000-0000")
    
    with p2:
        st.subheader("Servicios")
        st.write("Diseño de aplicaciones")
        st.write("Automatización de procesos")
        st.write("Visualización de datos")
        
    with p3:
        st.subheader("Redes Sociales")
        st.markdown("[YOUTUBE](https://www.youtube.com/watch?v=UI4f4iiVT6c)")
        st.markdown("[Facebook](https://www.youtube.com/watch?v=UI4f4iiVT6c)")
        st.markdown("[Instagram](https://www.youtube.com/watch?v=UI4f4iiVT6c)")
