"""
CP1404/CP5632 - Practical
Program for temperature conversion
"""

MENU = """MENU:
C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""


def main():
    """Convert temperature between celsius and fahrenheit"""
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            celsius = get_temperature("Celsius")
            fahrenheit = convert_celsius_to_fahrenheit(celsius)
            print(f"{celsius} C is {fahrenheit:.2f} F")
        elif choice == "F":
            fahrenheit = get_temperature("Fahrenheit")
            celsius = convert_fahrenheit_to_celsius(fahrenheit)
            print(f"{fahrenheit} F is {celsius:.2f} C")
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")


def get_temperature(unit):
    """Get temperature number"""
    number = float(input(f"Enter temperature in {unit}: "))
    return number


def convert_fahrenheit_to_celsius(fahrenheit):
    """Convert temperature from fahrenheit to celsius"""
    celsius = 5 / 9 * (fahrenheit - 32)
    return celsius


def convert_celsius_to_fahrenheit(celsius):
    """Convert temperature from celsius to fahrenheit"""
    fahrenheit = celsius * 9.0 / 5 + 32
    return fahrenheit


main()
