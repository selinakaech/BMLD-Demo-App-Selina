import streamlit as st
import pandas as pd

class DataManager:
    def __init__(self):
        if 'data_df' not in st.session_state:
            st.session_state['data_df'] = pd.DataFrame()

    def append_record(self, session_state_key, record_dict):
        if session_state_key in st.session_state:
            st.session_state[session_state_key] = st.session_state[session_state_key].append(record_dict, ignore_index=True)
        else:
            st.session_state[session_state_key] = pd.DataFrame([record_dict])

    def get_data(self, session_state_key):
        if session_state_key in st.session_state:
            return st.session_state[session_state_key]
        else:
            return None