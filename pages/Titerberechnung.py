import streamlit as st

def calculate_titer(dilution_factor, absorbance):
    return dilution_factor * absorbance

st.title("Titerberechnung")

st.sidebar.header("Eingabewerte")
dilution_factor = st.sidebar.number_input("Verdünnungsfaktor", min_value=1.0, step=0.1)
absorbance = st.sidebar.number_input("Absorption", min_value=0.0, step=0.01)

if st.sidebar.button("Berechnen"):
    titer = calculate_titer(dilution_factor, absorbance)
    st.write(f"Der berechnete Titer ist: {titer}")
else:
    st.write("Bitte geben Sie die Werte ein und klicken Sie auf 'Berechnen'.")