import random

print("1. Play the Number Guessing Game")
print("2. Exit")

try:
    choice = int(input("Enter your choice (1-2): "))
    if choice == 1:
        random_integer = random.randint(1, 100)
        counter = 0

        while True:
            try:
                guess = int(input("Guess the number between 1 - 100: "))
                counter += 1
                if guess == random_integer:
                    print(f"Congratulations! You guessed it in {counter} attempts!")
                    break
                elif guess > random_integer:
                    print("Too High! Try again.")
                elif guess < random_integer:
                    print("Too Low! Try again.")
            except ValueError:
                print("Invalid input! Please enter a valid number.")
    elif choice == 2:
        print("Exiting... Goodbye!")
    else:
        print("Invalid choice! Please select 1 or 2.")
except ValueError:
    print("Invalid input! Please enter a valid number.")