import streamlit as st
import pandas as pd

st.title("Meine erste Streamlit App")

st.write("Diese App wurde von Selina Käch entwickelt.")
st.write("E-Mail Adresse: kaechsel@students.zhaw.ch")

# Sidebar navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Gehe zu", ["Startseite", "Molmassenrechner", "Verdünnungsrechner"])

if page == "Startseite":
    st.write("Willkommen auf der Startseite!")
elif page == "Molmassenrechner":
    import pages.Molmassenrechner
elif page == "Verdünnungsrechner":
    import pages.Verdünnungsrechner