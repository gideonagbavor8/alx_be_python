# Author: Gideon Komla Agbavor
# Created: 12.06.2021
# Purpose: A simple tool to convert temperature from one unit to another

# Global Conversion Factors
FAHRENHEIT_TO_CELSIUS = 5/9
CELCIUS_TO_FAHRENHEIT = 9/5

# Convert Fahrenheit to Celsius
def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS

# Convert Celsius to Fahrenheit
def convert_to_fahrenheit(celsius):
    return (celsius * CELCIUS_TO_FAHRENHEIT) + 32

# User Interaction
def main():
    try:

        temperature = float(input("Enter the temperature to convert: "))
        unit = input("Is this temperature in Celcius or Fahrenheit? (C/F): ").strip().upper()

        if unit == "C":
            convert_temp = convert_to_fahrenheit(temperature)
            print(f"{temperature}°C is {convert_temp}°F")
        elif unit == "F":
            convert_temp = convert_to_celsius(temperature)
            print(f"{temperature}°F is {convert_temp}°C")
        else:
            print("Invalid unit. Please enter 'C' for Celcius or 'F' for Fahrenheit.")
    except ValueError as e:
        print(f"Error: {e}. Please enter a numeric value.")

if __name__ == "__main__":
    main()
