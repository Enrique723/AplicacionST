import streamlit as st 

Home = st.Page(
    page= "Vistas/Home.py",
    title= "Inicio",
    icon= ":material/home:",
    default= True,
)

Acercade = st.Page(
    page= "Vistas/Acercade.py",
    title= "Acerca de",
    icon= ":material/account_circle:",
    
)

project_1_page = st.Page(
    page= "Vistas/Ventas.py",
    title= "Ventas",
    icon= ":material/account_circle:",
)

project_2_page = st.Page(
    page= "Vistas/Chatbot.py",
    title= "Chat Bot",
    icon= ":material/smart_toy:",
)

pg = st.navigation(
    {
        "Informacion:": [Home,Acercade],
        "Proyectos:": [project_1_page, project_2_page],
    }
)

st.logo("Img/robot.png")
st.sidebar.markdown("Elaborado con el wacho por [Streamlit](https://streamit.io/gallery)")

pg.run()