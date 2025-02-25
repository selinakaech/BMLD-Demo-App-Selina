import streamlit as st
import requests

st.title("Molmassenrechner")

element = st.text_input("Gib das Elementsymbol ein (z.B. H für Wasserstoff):")

if st.button("Berechne Molmasse"):
    if element:
        response = requests.get(f"https://periodictableapi.herokuapp.com/api/v1/elements/{element}")
        if response.status_code == 200:
            data = response.json()
            molmasse = data.get("atomic_mass", "Nicht verfügbar")
            st.write(f"Die Molmasse von {element} ist {molmasse} g/mol.")
        else:
            st.write("Element nicht gefunden oder Fehler bei der Abfrage.")
    else:
        st.write("Bitte gib ein Elementsymbol ein.")

