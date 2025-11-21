import random

def play_game():
    while True:
        number = random.randint(1, 50)
        attempts = 0
        
        print("\nI'm thinking of a number between 1 and 50!")
        
        while True:
            try:
                guess = int(input("Enter your guess: "))
                attempts += 1
            except ValueError:
                print("Please enter a valid number!")
                continue

            if guess < number:
                print("Too low! Try again.")
            elif guess > number:
                print("Too high! Try again.")
            else:
                print(f"🎉 Correct! You guessed the number in {attempts} attempts.")
                break

        play_again = input("\nDo you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            print("Thanks for playing! Goodbye!")
            break

# Start the game
play_game()
