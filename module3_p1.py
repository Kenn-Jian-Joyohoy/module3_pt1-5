while True:
    print("\n=== Calculator ===")
    print("| 1. Add        |")
    print("| 2. Subtract   |")
    print("| 3. Multiply   |")
    print("| 4. Divide     |")
    print("| 5. Exit       |")
    print("==================")

    try:
        choice = int(input("Enter your choice (1-5): "))
        if choice == 1:
            a = int(input("Enter First Number: "))
            b = int(input("Enter Second Number: "))
            print(f"Result: {a} + {b} = {a + b}")
        elif choice == 2:
            a = int(input("Enter First Number: "))
            b = int(input("Enter Second Number: "))
            print(f"Result: {a} - {b} = {a - b}")
        elif choice == 3:
            a = int(input("Enter First Number: "))
            b = int(input("Enter Second Number: "))
            print(f"Result: {a} * {b} = {a * b}")
        elif choice == 4:
            a = int(input("Enter First Number: "))
            b = int(input("Enter Second Number: "))
            if b != 0:
                print(f"Result: {a} / {b} = {a / b}")
            else:
                print("Error: Division by zero is not allowed!")
        elif choice == 5:
            print("Thank you for using the calculator! Goodbye!")
            break
        else:
            print("Invalid choice! Please select a valid option (1-5).")
    except ValueError:
        print("Error: Please enter a valid number!")