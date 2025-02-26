import streamlit as st

def calculate_moles(mass, molar_mass):
    return mass / molar_mass

def calculate_mass(moles, molar_mass):
    return moles * molar_mass

def calculate_molar_mass(mass, moles):
    return mass / moles

st.title("Stoffmengenberechner")

mass = st.number_input("Masse (in Gramm):", min_value=0.0, step=0.1)
molar_mass = st.number_input("Molmasse (in g/mol):", min_value=0.0, step=0.1)
moles = st.number_input("Stoffmenge (in mol):", min_value=0.0, step=0.01)

if st.button("Berechnen"):
    if mass > 0 and molar_mass > 0:
        moles = calculate_moles(mass, molar_mass)
        st.write(f"Die Stoffmenge beträgt: {moles:.2f} mol")
    elif moles > 0 and molar_mass > 0:
        mass = calculate_mass(moles, molar_mass)
        st.write(f"Die Masse beträgt: {mass:.2f} g")
    elif mass > 0 and moles > 0:
        molar_mass = calculate_molar_mass(mass, moles)
        st.write(f"Die Molmasse beträgt: {molar_mass:.2f} g/mol")
    else:
        st.write("Bitte geben Sie mindestens zwei Werte ein, um den dritten zu berechnen.")