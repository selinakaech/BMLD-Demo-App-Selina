import streamlit as st
import pandas as pd
from utils.data_manager import DataManager

st.title("ChemCalc-App")
st.write("Diese Streamlit App ermöglicht die präzise Berechnung der Molmasse chemischer Verbindungen. Benutzer können die chemische Formel einer Verbindung eingeben, und die App berechnet automatisch die Molmasse basierend auf den Atommassen der enthaltenen Elemente.")

st.write("Diese App wurde von Selina Käch entwickelt.")
st.write("E-Mail Adresse: kaechsel@students.zhaw.ch")
