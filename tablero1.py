import pandas as pd
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(
    layout="centered",
    page_title="Talento Tech",
    page_icon=":shark:")

if "img" not in st.session_state:
    st.session_state.img = True

def print_campana(df):
    seleccion = st.session_state["select_box_campana"]
    with steps[2]:
        dataframe = ((df.loc[df["ID_Campana"] == seleccion]))
        st.dataframe(dataframe)

def btn_handler():
    st.session_state.img = not st.session_state.img

def btn2():
    st.session_state.boton_2 = not st.session_state.boton_2

t1, t2 = st.columns([0.3,0.7])

t2.title("Mi primer tablero")
t2.markdown(body="**tel:** 123")
t2.markdown("hola")
t2.title("Helow")
btn = t1.button("BOTON",on_click=btn_handler)
if (st.session_state.img):
    remi = t1.image("remi_editado.png", width=200)




#secciones

steps = st.tabs(["Pestaña 1","Pestaña 2", "Pestaña 3","Pestaña 4", "Pestaña 5"])
with steps[0]:
    st.write("Hola Mundo")
    st.image("sasha.png",width=400)
    data = {"Nombre":["Adan","Eva"], "Fecha de nacimiento":[0,0]}
    df = pd.DataFrame(data)
    st.table(df)
    st.dataframe(df)


with steps[1]:
    texto_boton_2 = "Mostrar texto" if not st.session_state.boton_2 else "Ocultar texto"
    st.button(texto_boton_2,on_click=btn2)
    if "boton_2" not in st.session_state:
        st.session_state.boton_2 = False
        texto_boton_2 = "Mostrar texto"
    if st.session_state.boton_2:
        st.write("Usted presionó el botón")

with steps[2]:
    camp_df = pd.read_csv("Campanhas.csv", encoding="latin-1", sep=";")
    camp = st.selectbox("Escoge un ID de campaña", camp_df["ID_Campana"], help="Muestra las campañas existentes", on_change=print_campana, key="select_box_campana", args=(camp_df,))
    met_df = pd.read_csv("Metricas.csv", encoding="latin-1", sep=";")
    id1 = met_df[(met_df["ID_Campana"] == camp) | (met_df["ID_Campana"] == 1)]
    id2 = met_df[(met_df["ID_Campana"] == 2)]
    st.write("Métricas filtradas")
    m1, m2, m3 = st.columns([1,1,1])
    m1.metric(label="Métrica 1",value=sum(id1["Conversiones"]), delta=str(sum(id1["Rebotes"]))+" Total de rebotes", delta_color="inverse")
    m2.metric(label="Métrica 2", value=np.mean(id1["Impresiones"]), delta=str(np.mean(id1["Clics"]))+" Total de clics",delta_color="inverse")

with steps[3]:
    sel_x = st.selectbox("Escoge el ID de la Campana", set(met_df["ID_Campana"].to_list()))
    varx = met_df[met_df["ID_Campana"] == sel_x]["ID_Metrica"]
    vary = met_df[met_df["ID_Campana"] == sel_x]["Conversiones"]
    st.dataframe(varx)
    st.dataframe(vary)  
    fig, ax = plt.subplots()
    ax = sns.lineplot( x=varx, y=vary)
    st.pyplot(fig)
    

with steps[4]:
    df=pd.read_csv("https://raw.githubusercontent.com/diplomado-bigdata-machinelearning-udea/Curso1/master/s03/dataVentas2009.csv")
    df.Fecha = pd.to_datetime(df.Fecha, format = "%d/%m/%Y")
    df.set_index("Fecha",inplace=True)
    var_x = st.selectbox("Escoge la variable x", df.columns)
    fig, ax = plt.subplots()
    ax = sns.histplot(data=df, x=var_x)
    st.pyplot(fig)