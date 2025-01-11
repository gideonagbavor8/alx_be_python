# Define Global Conversion Factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

def convert_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius."""
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

def main():
    try:
        # User Interaction
        temp = float(input("Enter the temperature: "))
        unit = input("Is the temperature in (C)elsius or (F)ahrenheit? ").strip().upper()

        if unit == 'C':
            converted_temp = convert_to_fahrenheit(temp)
            print(f"{temp}°C is {converted_temp:.2f}°F")
        elif unit == 'F':
            converted_temp = convert_to_celsius(temp)
            print(f"{temp}°F is {converted_temp:.2f}°C")
        else:
            raise ValueError("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()