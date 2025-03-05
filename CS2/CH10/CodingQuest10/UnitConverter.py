# Function to convert length units
def convert_length(value, from_unit, to_unit):
    # Dictionary of length units and their conversion factors to meters
    length_units = {
        'm': 1,
        'km': 1000,
        'cm': 0.01,
        'mm': 0.001,
        'mi': 1609.34,
        'yd': 0.9144,
        'ft': 0.3048,
        'in': 0.0254,
        'shaun': 1.78
    }
    try:
        # Check if the provided units are supported
        if from_unit not in length_units or to_unit not in length_units:
            raise ValueError("Unsupported unit type for length conversion.")
        # Convert the value to the target unit
        return value * length_units[from_unit] / length_units[to_unit]
    except Exception as e:
        print(f"An error occurred: {e}")
        return None


# Function to convert weight units
def convert_weight(value, from_unit, to_unit):
    # Dictionary of weight units and their conversion factors to kilograms
    weight_units = {
        'kg': 1,
        'g': 0.001,
        'mg': 0.000001,
        'lb': 0.453592,
        'oz': 0.0283495
    }
    try:
        # Check if the provided units are supported
        if from_unit not in weight_units or to_unit not in weight_units:
            raise ValueError("Unsupported unit type for weight conversion.")
        # Convert the value to the target unit
        return value * weight_units[from_unit] / weight_units[to_unit]
    except Exception as e:
        print(f"An error occurred: {e}")
        return None


# Function to convert temperature units
def convert_temperature(value, from_unit, to_unit):
    try:
        # Convert from Celsius to other units
        if from_unit == 'c':
            if to_unit == 'f':
                return (value * 9 / 5) + 32
            elif to_unit == 'k':
                return value + 273.15
        # Convert from Fahrenheit to other units
        elif from_unit == 'f':
            if to_unit == 'c':
                return (value - 32) * 5 / 9
            elif to_unit == 'k':
                return (value - 32) * 5 / 9 + 273.15
        # Convert from Kelvin to other units
        elif from_unit == 'k':
            if to_unit == 'c':
                return value - 273.15
            elif to_unit == 'f':
                return (value - 273.15) * 9 / 5 + 32
        # Raise an error if the provided units are unsupported
        raise ValueError("Unsupported unit type for temperature conversion.")
    except Exception as e:
        print(f"An error occurred: {e}")
        return None


# Main function to handle user input and perform conversions
def main():
    print("Unit Converter")
    try:
        # Prompt the user for input values
        value = float(input("Enter the value to convert: "))
        from_unit = input(
            "Enter the unit to convert from (e.g., m, km, cm, mm, mi, yd, ft, in, kg, g, mg, lb, oz, c, f, k): "
        ).lower()
        to_unit = input("Enter the unit to convert to: ").lower()

        # Determine the type of conversion based on the units
        length_units = {'m', 'km', 'cm', 'mm', 'mi', 'yd', 'ft', 'in', 'shaun'}
        weight_units = {'kg', 'g', 'mg', 'lb', 'oz'}
        temperature_units = {'c', 'f', 'k'}

        if from_unit in length_units and to_unit in length_units:
            result = convert_length(value, from_unit, to_unit)
        elif from_unit in weight_units and to_unit in weight_units:
            result = convert_weight(value, from_unit, to_unit)
        elif from_unit in temperature_units and to_unit in temperature_units:
            result = convert_temperature(value, from_unit, to_unit)
        else:
            raise ValueError("Unsupported conversion type or mismatched units.")

        # Display the result if the conversion was successful
        if result is not None:
            print(f"{value} {from_unit} is equal to {result:.2f} {to_unit}")
        else:
            print("Conversion failed. Please try again.")
    except ValueError as e:
        print(f"Invalid input: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()