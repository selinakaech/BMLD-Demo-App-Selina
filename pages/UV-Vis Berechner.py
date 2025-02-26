import streamlit as st

def calculate_concentration(absorbance, dilution_factor, path_length, molar_absorptivity):
    """
    Calculate the concentration of a sample using the Lambert-Beer law.

    A = ε * c * l

    :param absorbance: The measured absorbance of the sample
    :param dilution_factor: The dilution factor of the sample
    :param path_length: The path length of the cuvette in cm
    :param molar_absorptivity: The molar absorptivity coefficient in L/(mol*cm)
    :return: The concentration of the sample in mol/L
    """
    concentration = absorbance / (molar_absorptivity * path_length)
    return concentration * dilution_factor

st.title('UV-Vis Berechner')

absorbance = st.number_input('Geben Sie die Absorption ein:', min_value=0.0, step=0.01)
dilution_factor = st.number_input('Geben Sie den Verdünnungsfaktor ein:', min_value=1.0, step=0.1)
path_length = st.number_input('Geben Sie die Weglänge der Küvette (cm) ein:', min_value=0.1, step=0.1)
molar_absorptivity = st.number_input('Geben Sie den molaren Absorptionskoeffizienten (L/(mol*cm)) ein:', min_value=0.1, step=0.1)

if st.button('Berechnen'):
    concentration = calculate_concentration(absorbance, dilution_factor, path_length, molar_absorptivity)
    st.write(f'Die Konzentration der Probe beträgt {concentration} mol/L')