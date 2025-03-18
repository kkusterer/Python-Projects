def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def kelven_to_fahrenheit(kelven):
    return (kelven - 273)

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

choice = input("Choose an option (1, 2, 3): ")

if choice == '1':
        celsius = float(input("Enter temperature in Celsius: "))
        fahrenheit = celsius_to_fahrenheit(celsius)
        print(f"{celsius}°C is {fahrenheit}°F")

elif choice == '2':
        kelven = float(input("Enter temperature in kelven: "))
        celsius = kelven_to_fahrenheit(kelven)
        print(f"{kelven}°K is {kelven}°F")
