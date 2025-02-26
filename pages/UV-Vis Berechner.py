import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

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

# Kalibrationsdaten eingeben
st.write("Kalibrationsdaten eingeben:")
num_points = st.number_input('Anzahl der Kalibrationspunkte:', min_value=2, step=1, value=5)

calibration_data = []
for i in range(num_points):
    cal_absorbance = st.number_input(f'Absorption Punkt {i+1}:', min_value=0.0, step=0.01, key=f'abs_{i}')
    cal_concentration = st.number_input(f'Konzentration Punkt {i+1} (mol/L):', min_value=0.0, step=0.01, key=f'conc_{i}')
    calibration_data.append((cal_absorbance, cal_concentration))

if st.button('Kalibrationsgerade erstellen'):
    if len(calibration_data) >= 2:
        df = pd.DataFrame(calibration_data, columns=['Absorption', 'Konzentration'])
        X = df['Konzentration'].values.reshape(-1, 1)
        y = df['Absorption'].values

        model = LinearRegression()
        model.fit(X, y)
        slope = model.coef_[0]
        intercept = model.intercept_

        st.write(f'Kalibrationsgerade: Absorption = {slope:.4f} * Konzentration + {intercept:.4f}')

        # Plot der Kalibrationsgerade
        plt.figure(figsize=(10, 6))
        plt.scatter(df['Konzentration'], df['Absorption'], color='blue', label='Kalibrationspunkte')
        plt.plot(df['Konzentration'], model.predict(X), color='red', label='Kalibrationsgerade')
        plt.xlabel('Konzentration (mol/L)')
        plt.ylabel('Absorption')
        plt.title('Kalibrationsgerade')
        plt.legend()
        st.pyplot(plt)
    else:
        st.write('Bitte geben Sie mindestens zwei Kalibrationspunkte ein.')