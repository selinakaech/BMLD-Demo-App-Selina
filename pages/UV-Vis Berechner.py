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

# Example usage
absorbance = float(input("Enter the absorbance: "))
dilution_factor = float(input("Enter the dilution factor: "))
path_length = float(input("Enter the path length of the cuvette (cm): "))
molar_absorptivity = float(input("Enter the molar absorptivity coefficient (L/(mol*cm)): "))

concentration = calculate_concentration(absorbance, dilution_factor, path_length, molar_absorptivity)
print(f"The concentration of the sample is {concentration} mol/L")