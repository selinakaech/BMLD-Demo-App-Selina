import streamlit as st
import pandas as pd

from utils.data_manager import DataManager

# initialize the data manager
data_manager = DataManager(fs_protocol='webdav', fs_root_folder="BMLD_App_DB")  # switch drive 

# load the data from the persistent storage into the session state
data_manager.load_app_data(
    session_state_key='data_df', 
    file_name='data.csv', 
    initial_value = pd.DataFrame(), 
    parse_dates = ['timestamp']
    )

st.title("ChemCalc-App")
st.write("Diese Streamlit App ermöglicht die präzise Berechnung der Molmasse chemischer Verbindungen. Benutzer können die chemische Formel einer Verbindung eingeben, und die App berechnet automatisch die Molmasse basierend auf den Atommassen der enthaltenen Elemente.")

st.write("Diese App wurde von Selina Käch entwickelt.")
st.write("E-Mail Adresse: kaechsel@students.zhaw.ch")
