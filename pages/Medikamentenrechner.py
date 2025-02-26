import streamlit as st

def calculate_ibuprofen(weight):
    return weight * 10  # mg per kg

def calculate_dafalgan(weight):
    return weight * 15  # mg per kg

def calculate_diclofenac(weight):
    return weight * 2  # mg per kg

st.title("Medikamentenrechner")

weight = st.number_input("Geben Sie Ihr Körpergewicht in kg ein:", min_value=0.0, step=0.1)

if weight > 0:
    ibuprofen_dose = calculate_ibuprofen(weight)
    dafalgan_dose = calculate_dafalgan(weight)
    diclofenac_dose = calculate_diclofenac(weight)

    st.write(f"Empfohlene Ibuprofen-Dosis: {ibuprofen_dose} mg")
    st.write(f"Empfohlene Dafalgan-Dosis: {dafalgan_dose} mg")
    st.write(f"Empfohlene Diclofenac-Dosis: {diclofenac_dose} mg")
else:
    st.write("Bitte geben Sie ein gültiges Körpergewicht ein.")
    