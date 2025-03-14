# ====== Start Login Block ======
from utils.login_manager import LoginManager
LoginManager().go_to_login('Start.py') 
# ====== End Login Block ======

import streamlit as st
import pandas as pd

st.title('Molmassenwerte')

data_df = st.session_state['data_df']
if data_df.empty:
    st.info('Keine Molmassen vorhanden. Berechnen Sie Ihre Molmasse auf der Startseite.')
    st.stop()

# Überprüfe und bereinige die Daten
if 'timestamp' in data_df.columns:
    data_df['timestamp'] = pd.to_datetime(data_df['timestamp'], errors='coerce')
else:
    st.error('Die Spalte "timestamp" fehlt in den Daten.')
    st.stop()

if 'molmass' in data_df.columns:
    data_df['molmass'] = pd.to_numeric(data_df['molmass'], errors='coerce')
else:
    st.error('Die Spalte "molmass" fehlt in den Daten.')
    st.stop()

# Entferne Zeilen mit ungültigen Daten
data_df = data_df.dropna(subset=['timestamp', 'molmass'])

# Sort dataframe by timestamp
data_df = data_df.sort_values('timestamp', ascending=False)

# Display table
st.dataframe(data_df)