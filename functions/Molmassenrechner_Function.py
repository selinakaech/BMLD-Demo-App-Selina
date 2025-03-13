from utils import helpers

def calculate_molar_mass(elements, masses, timezone='Europe/Zurich'):
    """
    Calculate the molar mass and return a dictionary with inputs, molar mass, and timestamp.

    Args:
        elements (list): List of elements.
        masses (list): List of masses corresponding to the elements.

    Returns:
        dict: A dictionary containing the inputs, calculated molar mass, and timestamp.
    """
    if len(elements) != len(masses):
        raise ValueError("The length of elements and masses lists must be the same.")

    molar_mass = sum(masses)

    return {
        "timestamp": helpers.ch_now(),
        "elements": elements,
        "masses": masses,
        "molar_mass": round(molar_mass, 2),
    }

# Example usage
elements = ['H', 'O']
masses = [1.008, 15.999]
result = calculate_molar_mass(elements, masses)
print(result)