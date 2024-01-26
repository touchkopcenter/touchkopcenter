from asyncio import Server
import altair as alt
import numpy as np
import pandas as pd
import streamlit as st
from streamlit_gsheets import GSheetsConnection
#from streamlit_login_auth_ui.widgets import __login__
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader

with open('config.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)

authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['preauthorized']
)

@st.cache_data
#data_load_state.text("Done! (using st.cache_data)") 
def load_data(fdata:any):
    url = "https://docs.google.com/spreadsheets/d/1Rj0nYWOHMoVavnaMyroj-4PHdJeaTvZw8Mb4CTxyU0w/edit?usp=sharing"
    conn = st.connection("gsheets", type=GSheetsConnection)
    data = conn.read(spreadsheet=url, usecols=[1,4,7,8],ttl="0")

    
    # sortdata = data['ID'].where(data['ID']==fdata)
    sortdata = data.loc[data['ID']==fdata]
    if len(sortdata) > 0:
        st.dataframe(sortdata.dropna())
    else: st.write("No Data found")

    # sdata = data.loc[data['ID']=='7576927']
    # st.write(sdata)
    # st.write(len(sdata))

    
    # st.write(data.groupby("Name").count())

    #st.dataframe(data)

def clear_cache():
   #st.cache()
   st.cache_data.clear()



hashed_passwords = stauth.Hasher(['abc', 'def']).generate()
authenticator.login('Login', 'main')

if st.session_state["authentication_status"]:
    authenticator.logout('Logout', 'main', key='unique_key')
    st.write(f'Welcome *{st.session_state["name"]}*')
    st.title('Some content')
    st.button("Refresh Program",on_click=clear_cache)
    keyss = st.session_state["name"]
    st.write(keyss)

    title = st.text_input('')
    # title = keyss
    st.write('Search for ', title)
    # st.button("Find Data",on_click=load_data(title))
    load_data(str(keyss))

elif st.session_state["authentication_status"] is False:
    st.error('Username/password is incorrect')
elif st.session_state["authentication_status"] is None:
    st.warning('Please enter your username and password')
#st.text(hashed_passwords)



# @st.cache_data
# #data_load_state.text("Done! (using st.cache_data)") 
# def load_data():
#     url = "https://docs.google.com/spreadsheets/d/1Rj0nYWOHMoVavnaMyroj-4PHdJeaTvZw8Mb4CTxyU0w/edit?usp=sharing"
#     conn = st.experimental_connection("gsheets", type=GSheetsConnection)
#     data = conn.read(spreadsheet=url, usecols=[0, 1],ttl="0")
#     st.dataframe(data)
# def clear_cache():
#    #st.cache()
#    st.cache_data.clear()
# st.button("Refresh Program",on_click=clear_cache)
# load_data()


   
   



#jkjkjkjkkjkkkjj

