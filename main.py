import random

def get_computer_choice():
    choices = ['Rock', 'Paper', 'Scissors']
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'Rock' and computer_choice == 'Scissors') or \
         (user_choice == 'Scissors' and computer_choice == 'Paper') or \
         (user_choice == 'Paper' and computer_choice == 'Rock'):
        return "You win!"
    else:
        return "You lose!"

def display_result(user_choice, computer_choice, result):
    print(f"\nYou chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")
    print(result)

def play_again():
    while True:
        play_more = input("\nDo you want to play another round? (yes/no): ").lower()
        if play_more in ['yes', 'no']:
            return play_more == 'yes'
        print("Please type 'yes' or 'no'.")

def play_game():
    user_score = 0
    computer_score = 0

    while True:
        print("\n--- Rock, Paper, Scissors ---")
        user_choice = input("Enter your choice (Rock, Paper, Scissors): ").capitalize()

        if user_choice not in ['Rock', 'Paper', 'Scissors']:
            print("Invalid choice. Please choose Rock, Paper, or Scissors.")
            continue

        computer_choice = get_computer_choice()
        result = determine_winner(user_choice, computer_choice)
        display_result(user_choice, computer_choice, result)

        # Score tracking
        if result == "You win!":
            user_score += 1
        elif result == "You lose!":
            computer_score += 1

        print(f"\nScore -> You: {user_score} | Computer: {computer_score}")

        if not play_again():
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    play_game()
