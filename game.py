import random

def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "It's a tie!"
    elif (player_choice == 'rock' and computer_choice == 'scissors') or \
         (player_choice == 'paper' and computer_choice == 'rock') or \
         (player_choice == 'scissors' and computer_choice == 'paper'):
        return "You win!"
    else:
        return "Computer wins!"

def main():
    choices = ['rock', 'paper', 'scissors']

    while True:
        print("\nRock, Paper, Scissors Game")
        print("Enter your choice: rock, paper, or scissors (or q to quit)")
        player_choice = input("> ").lower()

        if player_choice == 'q':
            print("Thanks for playing!")
            break

        if player_choice not in choices:
            print("Invalid choice. Please enter rock, paper, or scissors.")
            continue

        computer_choice = random.choice(choices)
        print("Computer's choice:", computer_choice)

        print(determine_winner(player_choice, computer_choice))

if __name__ == "__main__":
    main()
