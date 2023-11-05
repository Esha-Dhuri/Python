#create a program that allows users to convert temperatures between Fahrenheit and Celsius in Python functions
def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def temperature():
    print("Temperature Converter")
    print("1. Fahrenheit to Celsius")
    print("2. Celsius to Fahrenheit")
    
    choice = int(input("Enter your choice: "))

    if choice == 1:
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        celsius = fahrenheit_to_celsius(fahrenheit)
        print(f"{fahrenheit}°F is {celsius}°C")
    elif choice == 2:
        celsius = float(input("Enter temperature in Celsius: "))
        fahrenheit = celsius_to_fahrenheit(celsius)
        print(f"{celsius}°C is {fahrenheit}°F")
    else:
        print("Invalid choice. Please select 1 or 2.")

temperature()
