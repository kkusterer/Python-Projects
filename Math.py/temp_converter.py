def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32


def kelven_to_fahrenheit(k):
    return ((k - 273.15) * 9/5 + 32)


def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9


def main():
    print("Temperature Converter")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Kelven to Fahrenheit")

    choice = input("Choose an option (1, 2, 3): ")

    if choice == '1':
        celsius = float(input("Enter temperature in Celsius: "))
        fahrenheit = celsius_to_fahrenheit(celsius)
        print(f"{celsius}°C is {fahrenheit}°F")

    elif choice == '2':
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        celsius = fahrenheit_to_celsius(fahrenheit)
        print(f"{fahrenheit}°F is {celsius}°C")

    elif choice == '3':
        k = float(input("Enter temperature in Kelven: "))
        fahrenheit = kelven_to_fahrenheit(k)
        print(f"{k}°K is {fahrenheit}°F")

    else:
        print("Invalid choice")


if __name__ == "__main__":
    main()
