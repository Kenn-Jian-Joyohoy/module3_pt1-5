print("=" * 30)
print("   Temperature Conversion   ")
print("=" * 30)

while True:
    print("\n------------- MENU -------------")
    print("1. Convert Celsius to Fahrenheit")
    print("2. Convert Fahrenheit to Celsius")
    print("3. Exit")
    print("-" * 30)

    try:
        choice = int(input("Enter your choice (1-3): "))
        print("-" * 30)

        if choice == 1:
            num1 = float(input("Enter temperature in Celsius: "))
            fahrenheit = (num1 * 9 / 5) + 32
            print(f"{num1}°C is equal to {fahrenheit:.2f}°F")
        elif choice == 2:
            num2 = float(input("Enter temperature in Fahrenheit: "))
            celsius = (num2 - 32) * (5 / 9)
            print(f"{num2}°F is equal to {celsius:.2f}°C")
        elif choice == 3:
            print("\nThank you for using the Temperature Converter!")
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Please select a valid option (1-3).")
    except ValueError:
        print("Error: Please enter a valid number!")