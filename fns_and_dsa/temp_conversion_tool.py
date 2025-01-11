# Author: Gideon Komla Agbavor
# Created: 12.06.2021
# Purpose: A simple tool to convert temperature from one unit to another

# temp_conversion_tool.py

# Global Conversion Factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

def convert_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius using the global conversion factor."""
    global FAHRENHEIT_TO_CELSIUS_FACTOR
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit using the global conversion factor."""
    global CELSIUS_TO_FAHRENHEIT_FACTOR
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

def main(): 

    temperature = float(input("Enter the temperature to convert: ")) 
    unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper() 
    if unit == 'C': 
        converted_temp = convert_to_fahrenheit(temperature) 
        print(f"{temperature}°C is {converted_temp}°F") 
    elif unit == 'F': 
        converted_temp = convert_to_celsius(temperature) 
        print(f"{temperature}°F is {converted_temp}°C") 
    else: 
        print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.") 
if __name__ == "__main__":
    main()
