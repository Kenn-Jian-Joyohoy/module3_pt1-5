print("1. Add Score")
print("2. Calculate Average")
print("3. Exit")

scores = []

while True:
    try:
        choice = int(input("Enter your choice: "))
        if choice == 1:
            new_score = int(input("Add Score: "))
            scores.append(new_score)
            print(f"Score {new_score} added!")
        elif choice == 2:
            if scores:
                average = sum(scores) / len(scores)
                print(f"Average Score: {average:.2f}")
            else:
                print("No scores available to calculate the average.")
        elif choice == 3:
            print("Goodbye!")
            exit()
        else:
            print("Invalid choice. Please try again.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")