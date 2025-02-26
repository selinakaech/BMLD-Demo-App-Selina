import streamlit as st

def calculate_bmi(weight, height):
    return weight / (height ** 2)

st.title("BMI Rechner")

weight = st.number_input("Gewicht (kg)", min_value=0.0, format="%.2f")
height = st.number_input("Größe (m)", min_value=0.0, format="%.2f")

if st.button("Berechnen"):
    if height > 0:
        bmi = calculate_bmi(weight, height)
        st.write(f"Ihr BMI ist: {bmi:.2f}")
        if bmi < 18.5:
            st.write("Untergewicht")
        elif 18.5 <= bmi < 24.9:
            st.write("Normalgewicht")
        elif 25 <= bmi < 29.9:
            st.write("Übergewicht")
        else:
            st.write("Adipositas")
    else:
        st.write("Bitte geben Sie eine gültige Größe ein.")