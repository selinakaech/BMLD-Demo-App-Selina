# ====== Start Init Block ======
# This needs to copied on top of the entry point of the app (Start.py)

import pandas as pd
from utils.data_manager import DataManager
from utils.login_manager import LoginManager

# initialize the data manager
data_manager = DataManager(fs_protocol='webdav', fs_root_folder="BMLD_Demo_App")  # switch drive 

# initialize the login manager
login_manager = LoginManager(data_manager)
login_manager.login_register()  # open login/register page

# load the data from the persistent storage into the session state
data_manager.load_user_data(
    session_state_key='data_df', 
    file_name='data.csv', 
    initial_value = pd.DataFrame(), 
    parse_dates = ['timestamp']
    )
# ====== End Init Block ======

import streamlit as st
import pandas as pd
from utils.data_manager import DataManager

st.title("ChemCalc-App")
st.write("Diese Streamlit App ermöglicht die präzise Berechnung der Molmasse chemischer Verbindungen. Benutzer können die chemische Formel einer Verbindung eingeben, und die App berechnet automatisch die Molmasse basierend auf den Atommassen der enthaltenen Elemente.")

st.write("Diese App wurde von Selina Käch entwickelt.")
st.write("E-Mail Adresse: kaechsel@students.zhaw.ch")
