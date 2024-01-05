from asyncio import Server
import altair as alt
import numpy as np
import pandas as pd
import streamlit as st
from streamlit_gsheets import GSheetsConnection


@st.cache_data 
def load_data():
    url = "https://docs.google.com/spreadsheets/d/1Rj0nYWOHMoVavnaMyroj-4PHdJeaTvZw8Mb4CTxyU0w/edit?usp=sharing"
    conn = st.experimental_connection("gsheets", type=GSheetsConnection)
    data = conn.read(spreadsheet=url, usecols=[0, 1])
    st.dataframe(data)

load_data()

def clear_cache():
   #st.cache()
   st.cache_data.clear()
   
   

st.sidebar.button("Refresh Program",on_click=clear_cache)

#jkjkjkjkkjkkkjj

