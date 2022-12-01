import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(page_title="BU - Users",
                    page_icon=":corn:",
                    layout="wide"
)

df = pd.read_excel(
    io='BU.xlsx',
    engine='openpyxl',
    sheet_name='Productores',
    usecols='A:S',
    nrows=1050,
)

# MAINPAGE
st.title(":floppy_disk: Listado de Users de BU")
st.dataframe(df)


# SIDEBAR

st.sidebar.header("Filtros de Base de Datos:")

owner = st.sidebar.multiselect(
    "Selecciona el Owner:",
    options=df["Owner"].unique(),
    default=df["Owner"].unique()
)

tokenizaron = st.sidebar.multiselect(
    "¿Tokenizaron?",
    options=df["Tokenizaron"].unique(),
    default=df["Tokenizaron"].unique()
)

solicitoVisa = st.sidebar.multiselect(
    "¿Solicitó Visa?",
    options=df["Solicitó VISA"].unique(),
    default=df["Solicitó VISA"].unique()
)