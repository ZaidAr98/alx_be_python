FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5




def convert_to_celsius(fahrenheit):
        
        celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
        print(f"{fahrenheit}°F is {celsius}°C")

def convert_to_fahrenheit(celsius):
 
          fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
          print(f"{celsius}°C is {fahrenheit}°F ")

temperature = input("Enter the temperature to convert:")

this_is   = input("Is this temperature in Celsius or Fahrenheit? (C/F):")


if isinstance(temperature, (int,float)):
       
    if this_is=="F":
        convert_to_celsius(temperature)
    elif this_is=="C":
        convert_to_fahrenheit(temperature)
else:
      print("Invalid temperature. Please enter a numeric value.")