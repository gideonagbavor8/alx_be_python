# temp_conversion_tool.py

# Global Conversion Factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

def convert_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius using the global conversion factor."""
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit using the global conversion factor."""
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

def main():
    # User Input
    temp_input = input("Enter the temperature followed by its unit (C for Celsius, F for Fahrenheit): ")
    
    try:
        # Extract temperature value and unit
        temp_value_str, temp_unit = temp_input[:-1], temp_input[-1].upper()
        temp_value = float(temp_value_str)
        
        # Validate temperature unit
        if temp_unit not in ['C', 'F']:
            print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
            return
        
        # Perform conversion based on unit
        if temp_unit == 'C':
            converted_temp = convert_to_fahrenheit(temp_value)
            print(f"{temp_value}°C is {converted_temp:.2f}°F")
        elif temp_unit == 'F':
            converted_temp = convert_to_celsius(temp_value)
            print(f"{temp_value}°F is {converted_temp:.2f}°C")
    except (IndexError, ValueError):
        print("Invalid input. Please enter a valid temperature and unit.")

if __name__ == "__main__":
    main()
