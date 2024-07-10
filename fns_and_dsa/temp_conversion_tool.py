FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5


def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR


def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32


def get_temperature_input():
    temperature = input("Enter the temperature to convert: ")
    try:
        temperature = float(temperature)
    except ValueError:
        raise ValueError("Invalid temperature. Please enter a numeric value.")
    return temperature


def get_unit_input():
    unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")
    if unit.upper() not in ['C', 'F']:
        raise ValueError(
            "Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
    return unit.upper()


def main():
    temperature = get_temperature_input()
    unit = get_unit_input()

    if unit == 'C':
        converted_temperature = convert_to_fahrenheit(temperature)
        print(f"{temperature}°C is {converted_temperature}°F")
    else:
        converted_temperature = convert_to_celsius(temperature)
        print(f"{temperature}°F is {converted_temperature}°C")


if __name__ == "__main__":
    main()
