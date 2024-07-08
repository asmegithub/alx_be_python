CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9


def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR


def convert_to_fahrenheit(celsius):
    return celsius * CELSIUS_TO_FAHRENHEIT_FACTOR + 32


input_temp = input("Enter the temperature to convert:")
try:
    input_temp = float(input_temp)
except ValueError:
    print("Invalid input. Please enter a valid number.")
    exit()

choice = input("Is this temperature in Celsius or Fahrenheit? (C/F):")
match choice.capitalize():
    case "F":
        print(convert_to_celsius(input_temp))
    case "C":
        print(convert_to_fahrenheit(input_temp))
    case _:
        print("Invalid choice. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
