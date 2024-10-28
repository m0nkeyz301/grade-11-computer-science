def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5)+ 32
    print(fahrenheit)

celsius = int(input("Enter a temperature in celsius: "))
celsius_to_fahrenheit(celsius)