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
data_df['timestamp'] = pd.to_datetime(data_df['timestamp'], errors='coerce')
data_df['molmass'] = pd.to_numeric(data_df['molmass'], errors='coerce')

# Entferne Zeilen mit ungültigen Daten
data_df = data_df.dropna(subset=['timestamp', 'molmass'])

# Sort dataframe by timestamp
data_df = data_df.sort_values('timestamp', ascending=False)

# Display table
st.dataframe(data_df)