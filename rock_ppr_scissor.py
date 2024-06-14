import random

def get_user_choice():
    choices = ["rock", "paper", "scissors"]
    user_choice = input("Enter your choice (rock, paper, scissors): ").lower()
    while user_choice not in choices:
        print("Invalid choice. Please choose rock, paper, or scissors.")
        user_choice = input("Enter your choice (rock, paper, scissors): ").lower()
    return user_choice

def get_computer_choice():
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)

def determine_winner(user_choice, comp_choice):
    if user_choice == comp_choice:
        return "It's a tie!"
    elif (user_choice == "rock" and comp_choice == "scissors") or \
         (user_choice == "paper" and comp_choice == "rock") or \
         (user_choice == "scissors" and comp_choice == "paper"):
        return "You win!"
    else:
        return "You lose!"

def play_game():
    print("Welcome to Rock-Paper-Scissors!")
    user_choice = get_user_choice()
    comp_choice = get_computer_choice()
    print(f"Your choice: {user_choice}")
    print(f"Computer's choice: {comp_choice}")
    result = determine_winner(user_choice, comp_choice)
    print(result)

if __name__ == "__main__":
    play_game()
