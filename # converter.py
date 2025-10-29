# converter.py
def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

def celsius_to_kelvin(c):
    return c + 273.15

def kelvin_to_celsius(k):
    return k - 273.15

if __name__ == "__main__":
    print("🌡️  Temperature Converter 🌡️")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Celsius to Kelvin")
    print("4. Kelvin to Celsius")

    choice = int(input("Enter your choice (1-4): "))
    temp = float(input("Enter temperature value: "))

    if choice == 1:
        print(f"{temp}°C = {celsius_to_fahrenheit(temp):.2f}°F")
    elif choice == 2:
        print(f"{temp}°F = {fahrenheit_to_celsius(temp):.2f}°C")
    elif choice == 3:
        print(f"{temp}°C = {celsius_to_kelvin(temp):.2f}K")
    elif choice == 4:
        print(f"{temp}K = {kelvin_to_celsius(temp):.2f}°C")
    else:
        print("Invalid choice!")
