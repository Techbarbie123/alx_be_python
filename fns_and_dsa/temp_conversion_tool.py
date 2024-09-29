FAHRENHEIT_TO_CELSIUS_FACTOR = 5 /9
CELSIUS_TO_FAHRENHEIT_FACTOR  = 9 /5
def celsius_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
def fahrenheit_to_celsius(fahreheit):
    return (fahreheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
def main():
    temp = float(input( "enter the temperature to convert:"))
    try:
        num = float(temp)
    except ValueError:
        print("invalid temperature. please enter a numeric value.")
    unit = input("is this temperature in celsius or fahrenheit? (C/F):").strip().upper()
    if unit == "C":
        converted_temp = celsius_to_fahrenheit
        print(f"{temp}°C is {converted_temp}°F")
    elif unit == "F":
        converted_temp = fahrenheit_to_celsius
        print(f"{temp}°F is {converted_temp}°C")
    else:
        print("invalid unit, enter C for celsius or F for fahrenheit")
main()