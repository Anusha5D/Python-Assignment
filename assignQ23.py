temperature = float(input("Enter temperature: "))
unit = input("Enter unit (C for Celsius, F for Fahrenheit): ")
if unit == 'C':
    fahrenheit = (temperature * 9/5) + 32
    print(f"{temperature}°C is equal to {fahrenheit}°F")
elif unit == 'F':
    celsius = (temperature - 32) * 5/9
    print(f"{temperature}°F is equal to {celsius}°C")
else:
    print("Invalid unit. Please enter C or F.")
