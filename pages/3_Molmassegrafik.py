# ====== Start Login Block ======
from utils.login_manager import LoginManager
LoginManager().go_to_login('Start.py') 
# ====== End Login Block ======

import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

st.title('Molmassenwerte')

# Überprüfen, ob die Daten im Session-State vorhanden sind
if 'data_df' not in st.session_state:
    st.error('Daten nicht gefunden. Bitte laden Sie die Daten auf der Startseite.')
    st.stop()

data_df = st.session_state['data_df']
if data_df.empty:
    st.info('Keine Molmassen vorhanden. Berechnen Sie Ihre Molmasse auf der Startseite.')
    st.stop()

# Molmasse über Zeit
st.line_chart(data=data_df.set_index('timestamp')['molmass'], 
                use_container_width=True)
st.caption('Molmasse über Zeit (g/mol)')

# Histogramm der Molmassenverteilung
st.subheader('Verteilung der Molmassen')
fig, ax = plt.subplots()
sns.histplot(data_df['molmass'], bins=20, kde=True, ax=ax)
ax.set_xlabel('Molmasse (g/mol)')
ax.set_ylabel('Häufigkeit')
st.pyplot(fig)

# Boxplot der Molmassen
st.subheader('Boxplot der Molmassen')
fig, ax = plt.subplots()
sns.boxplot(x=data_df['molmass'], ax=ax)
ax.set_xlabel('Molmasse (g/mol)')
st.pyplot(fig)

# Scatterplot von Molmasse gegen Zeit
st.subheader('Molmasse gegen Zeit')
fig, ax = plt.subplots()
sns.scatterplot(x=data_df['timestamp'], y=data_df['molmass'], ax=ax)
ax.set_xlabel('Zeit')
ax.set_ylabel('Molmasse (g/mol)')
st.pyplot(fig)