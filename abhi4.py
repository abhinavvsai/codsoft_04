import random

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "You win!"
    else:
        return "You lose!"

def display_result(user_choice, computer_choice, result):
    print(f"\nYou chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")
    print(result)

def main():
    user_score = 0
    computer_score = 0

    while True:
        print("\nRock, Paper, Scissors Game")
        print("Enter your choice (rock, paper, or scissors):")
        user_choice = input().lower()

        if user_choice not in ["rock", "paper", "scissors"]:
            print("Invalid choice. Please try again.")
            continue

        computer_choice = get_computer_choice()
        result = determine_winner(user_choice, computer_choice)
        
        display_result(user_choice, computer_choice, result)

        if result == "You win!":
            user_score += 1
        elif result == "You lose!":
            computer_score += 1

        print(f"\nCurrent Score: You - {user_score}, Computer - {computer_score}")

        play_again = input("\nDo you want to play another round? (yes/no): ").lower()
        if play_again != "yes":
            break

    print(f"\nFinal Score: You - {user_score}, Computer - {computer_score}")
    print("Thanks for playing!")

if __name__ == "__main__":
    main()
