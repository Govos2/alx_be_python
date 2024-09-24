FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5
def convert_to_celsius(fahrenheit):
    global FAHRENHEIT_TO_CELSIUS_FACTOR
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
def convert_to_fahrenheit(celsius):
    global CELSIUS_TO_FAHRENHEIT_FACTOR
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
def main():
    try:
        temp = input("Enter the temperature value: ")
        unit = input("Is the temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()
        if not temp.replace('.', '', 1).isdigit():
            raise ValueError("Invalid temperature. Please enter a numeric value.")
        temp = float(temp)
        if unit == "C":
            print(f"{temp} Celsius is {convert_to_fahrenheit(temp):.2f} Fahrenheit.")
        elif unit == "F":
            print(f"{temp} Fahrenheit is {convert_to_celsius(temp):.2f} Celsius.")
        else:
            print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
    except ValueError as e:
        print(e)
