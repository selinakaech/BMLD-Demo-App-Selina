import streamlit as st
import pandas as pd
from utils.data_manager import DataManager

st.title('Molmassendaten')

# Load data from session state
data_df = DataManager().get_data(session_state_key='data_df')

if data_df is not None and not data_df.empty:
    st.write(data_df)
else:
    st.write("Keine Daten verfügbar.")