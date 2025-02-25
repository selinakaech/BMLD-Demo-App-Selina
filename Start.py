import streamlit as st
import pandas as pd

st.title("Meine erste Streamlit App")

st.write("Diese App wurde von Selina Käch entwickelt.")
st.write("E-Mail Adresse: kaechsel@students.zhaw.ch")

# Link zur Molmassenrechner-Seite
if st.button("Gehe zu Molmassenrechner"):
    st.experimental_rerun()
    st.write("pages/Molmassenrechner.py")