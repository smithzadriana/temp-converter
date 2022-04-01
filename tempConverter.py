#author: Zadriana Smith
#date: 02/28/2021
#description: converts between Celsius and Fahrenheit; converts celsius to kelvins

celsius = int (input("Enter the temperature in degrees Celsius: " ))

convert_to_fahrenheit = celsius * 9 / 5 + 32

print("The temperature in Fahrenheit is", convert_to_fahrenheit, "degrees Fahrenheit")

fahrenheit = int (input("Enter the temperature in degrees Fahrenheit: "))

convert_to_celsius = fahrenheit - 32
convert_to_celsius = convert_to_celsius * 5 / 9

print("The temperature in Celsius is", convert_to_celsius, "degrees Celsius")

kelvin = int (input("To convert from Celsius to Kelvin, enter temperature in degrees Celsius: "))

convert_to_kelvin = kelvin + 273.15

print ("The temperature in Kelvin is", convert_to_kelvin, "K")

