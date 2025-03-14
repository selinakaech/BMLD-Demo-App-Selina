# ====== Start Login Block ======
from utils.login_manager import LoginManager
LoginManager().go_to_login('Start.py') 
# ====== End Login Block ======

import streamlit as st
import pandas as pd
import altair as alt
from functions.Molmassen_Calculator import create_result_dict
from utils.data_manager import DataManager

st.title('Molmassenrechner')

# Initialize the session state key if it doesn't exist
if 'data_df' not in st.session_state:
    st.session_state['data_df'] = pd.DataFrame()

with st.form(key='element_form'):
    compound = st.text_input('Geben Sie die chemische Verbindung ein (z.B. H2O):')
    multiplier = st.number_input('Geben Sie die entsprechende Menge der chemischen Verbindung ein:', min_value=1, value=1)
    submit_button = st.form_submit_button(label='Berechnen')

if submit_button:
    if compound:
        result = create_result_dict(compound, multiplier)
        if 'error' not in result:
            st.write(f'Die Molmasse der Verbindung {compound} multipliziert mit {multiplier} ist {result["molar_mass"]} g/mol.')

            # Create a DataFrame for the bar chart
            df = pd.DataFrame(result['element_masses'], columns=['Element', 'Masse'])
            chart = alt.Chart(df).mark_bar().encode(
                x='Element',
                y='Masse'
            ).properties(
                title='Molmasse der Elemente in der Verbindung'
            )
            st.altair_chart(chart, use_container_width=True)
        else:
            st.write(result['error'])

        

# Add a reset button to clear the input fieldss
if st.button('Zurücksetzen'):
    st.experimental_rerun()

 # ---Save BMI data ---
from utils.data_manager import DataManager
DataManager().append_record(session_state_key='data_df', record_dict=result)  # update data in session state and storage