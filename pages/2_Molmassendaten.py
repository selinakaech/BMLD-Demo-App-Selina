# ====== Start Login Block ======
from utils.login_manager import LoginManager
LoginManager().go_to_login('Start.py') 
# ====== End Login Block ======

import streamlit as st
import pandas as pd

st.title('Molmassenwerte')

# Überprüfen, ob die Daten im Session-State vorhanden sind
if 'data_df' not in st.session_state:
    st.error('Daten nicht gefunden. Bitte laden Sie die Daten auf der Startseite.')
    st.stop()

data_df = st.session_state['data_df']
if data_df.empty:
    st.info('Keine Molmassen vorhanden. Berechnen Sie Ihre Molmasse auf der Startseite.')
    st.stop()

# Überprüfe und bereinige die Daten
required_columns = ['timestamp', 'molmass', 'weight', 'height']
missing_columns = [col for col in required_columns if col not in data_df.columns]

if missing_columns:
    st.error(f'Die folgenden Spalten fehlen in den Daten: {", ".join(missing_columns)}')
    st.stop()

data_df['timestamp'] = pd.to_datetime(data_df['timestamp'], errors='coerce')
data_df['molmass'] = pd.to_numeric(data_df['molmass'], errors='coerce')
data_df['weight'] = pd.to_numeric(data_df['weight'], errors='coerce')
data_df['height'] = pd.to_numeric(data_df['height'], errors='coerce')

# Entferne Zeilen mit ungültigen Daten
data_df = data_df.dropna(subset=required_columns)

# Sort dataframe by timestamp
data_df = data_df.sort_values('timestamp', ascending=False)

# Display table
st.dataframe(data_df)

# Histogramm der Molmassenverteilung
if 'molmass' in data_df.columns:
    st.subheader('Verteilung der Molmassen')
    st.bar_chart(data_df['molmass'])   # create a bar chart
    st.caption('Molmasse (g/mol)')
else:
    st.error('Die Spalte "molmass" fehlt in den Daten.')