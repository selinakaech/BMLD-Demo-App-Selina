# ====== Start Login Block ======
from utils.login_manager import LoginManager
LoginManager().go_to_login('Start.py') 
# ====== End Login Block ======

import streamlit as st

st.title('Molmassenwerte')

data_df = st.session_state['data_df']
if data_df.empty:
    st.info('Keine Molmassen vorhanden. Berechnen Sie Ihre Molmasse auf der Startseite.')
    st.stop()

# Sort dataframe by timestamp
data_df = data_df.sort_values('timestamp', ascending=False)

# Display table
st.dataframe(data_df)