import streamlit as st

st.title("Stoffmengenrechner")

# Eingabe der Molmasse
molmasse = st.number_input("Gib die Molmasse in g/mol ein:", min_value=0.0, format="%.2f")

# Eingabe der Masse
masse = st.number_input("Gib die Masse in g ein:", min_value=0.0, format="%.2f")

if st.button("Berechne Stoffmenge"):
    try:
        if molmasse > 0 and masse > 0:
            stoffmenge = masse / molmasse
            st.write(f"Die Stoffmenge beträgt {stoffmenge:.4f} mol.")
        else:
            st.error("Bitte gib gültige Werte für Molmasse und Masse ein.")
    except Exception as e:
        st.error(f"Ein Fehler ist aufgetreten: {e}")