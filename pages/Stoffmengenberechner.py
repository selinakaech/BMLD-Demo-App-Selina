import streamlit as st

def calculate_moles(mass, molar_mass):
    return mass / molar_mass

st.title("Stoffmengenberechner")

mass = st.number_input("Masse (in Gramm):", min_value=0.0, step=0.1)
molar_mass = st.number_input("Molmasse (in g/mol):", min_value=0.0, step=0.1)

if st.button("Berechnen"):
    if molar_mass > 0:
        moles = calculate_moles(mass, molar_mass)
        st.write(f"Die Stoffmenge beträgt: {moles:.2f} mol")
    else:
        st.write("Bitte geben Sie eine gültige Molmasse ein.")