import streamlit as st

st.title("Multiplikation von zwei Zahlen")

def multipliziere(a, b):
    return a * b

zahl1 = st.number_input("Gib die erste Zahl ein:", value=0.0)
zahl2 = st.number_input("Gib die zweite Zahl ein:", value=0.0)

if st.button("Multiplizieren"):
    ergebnis = multipliziere(zahl1, zahl2)
    st.write(f"Das Ergebnis der Multiplikation von {zahl1} und {zahl2} ist {ergebnis}.")