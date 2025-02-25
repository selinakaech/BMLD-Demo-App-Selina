import streamlit as st

st.title("Verdünnungsrechner")

st.header("Verdünnungsrechner")

# Eingabe der Konzentrationen und Volumina
c1 = st.number_input("Konzentration der Stammlösung (c1) in mol/L", min_value=0.0, step=0.01)
v1 = st.number_input("Volumen der Stammlösung (v1) in L", min_value=0.0, step=0.01)
c2 = st.number_input("Gewünschte Endkonzentration (c2) in mol/L", min_value=0.0, step=0.01)

# Berechnung des Endvolumens
if c1 > 0 and c2 > 0:
    v2 = (c1 * v1) / c2
    st.write(f"Das benötigte Endvolumen (v2) ist {v2:.2f} L")
else:
    st.write("Bitte geben Sie gültige Werte für c1 und c2 ein.")

