# CELSIUS_TO_FAHRENHEIT_FACTOR = 9.0 / 5.0
# FAHRENHEIT_TO_CELSIUS_FACTOR = 5.0 / 9.0


# def convert_to_celsius(fahrenheit):
#     return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR


# def convert_to_fahrenheit(celsius):
#     return celsius * CELSIUS_TO_FAHRENHEIT_FACTOR + 32


# input_temp = input("Enter the temperature to convert: ")
# try:
#     input_temp = float(input_temp)
# except ValueError:
#     print("Invalid input. Please enter a valid number.")
#     exit()


# choice = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").capitalize()
# match choice:
#     case "F":
#         print(
#             f"{input_temp} degrees Fahrenheit is {convert_to_celsius(input_temp)} degrees Celsius."
#         )
#     case "C":
#         print(
#             f"{input_temp} degrees Celsius is {convert_to_fahrenheit(input_temp)} degrees Fahrenheit."
#         )
#     case _:
#         print("Invalid choice. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
CELSIUS_TO_FAHRENHEIT_FACTOR = 9.0 / 5.0
FAHRENHEIT_TO_CELSIUS_FACTOR = 5.0 / 9.0


def validate_input(temp):
    try:
        return float(temp)
    except ValueError:
        raise ValueError("Invalid temperature. Please enter a numeric value.")


def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR


def convert_to_fahrenheit(celsius):
    return celsius * CELSIUS_TO_FAHRENHEIT_FACTOR + 32


input_temp = input("Enter the temperature to convert: ")
input_temp = validate_input(input_temp)

choice = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").capitalize()
if choice == "F":
    print(
        f"{input_temp} degrees Fahrenheit is {convert_to_celsius(input_temp)} degrees Celsius."
    )
elif choice == "C":
    print(
        f"{input_temp} degrees Celsius is {convert_to_fahrenheit(input_temp)} degrees Fahrenheit."
    )
else:
    print("Invalid choice. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
