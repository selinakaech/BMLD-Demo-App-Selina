# ====== Start Login Block ======
from utils.login_manager import LoginManager
LoginManager().go_to_login('Start.py') 
# ====== End Login Block ======

import streamlit as st
import matplotlib.pyplot as plt

st.title('Molmassenwerte')

# Überprüfen, ob die Daten im Session-State vorhanden sind
if 'data_df' not in st.session_state:
    st.error('Daten nicht gefunden. Bitte laden Sie die Daten auf der Startseite.')
    st.stop()

data_df = st.session_state['data_df']
if data_df.empty:
    st.info('Keine Molmassen vorhanden. Berechnen sie Ihre Molmasse auf der Startseite.')
    st.stop()

# Histogramm der Massen und Elemente
st.subheader('Verteilung der Massen und Elemente')
fig, ax = plt.subplots()
elements = data_df['element'].unique()
for element in elements:
    element_data = data_df[data_df['element'] == element]
    ax.hist(element_data['mass'], bins=20, alpha=0.5, label=element, edgecolor='black')
ax.set_xlabel('Masse (g/mol)')
ax.set_ylabel('Häufigkeit')
ax.legend(title='Element')
st.pyplot(fig)