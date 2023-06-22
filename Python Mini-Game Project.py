import random

# Function to validate user input


def validate_input(user_input):
    if user_input.lower() in ['rock', 'paper', 'scissors']:
        return True
    else:
        return False

# Function to generate computer's choice


def generate_computer_choice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

# Function to apply game rules and determine the winner


def get_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (
        (user_choice == 'rock' and computer_choice == 'scissors') or
        (user_choice == 'paper' and computer_choice == 'rock') or
        (user_choice == 'scissors' and computer_choice == 'paper')
    ):
        return "Congratulations! You win!"
    else:
        return "Sorry! Computer wins!"


# Main game loop
while True:
    # Taking input from the user
    user_input = input("Enter your choice (rock/paper/scissors): ")

    # Validating user input
    if not validate_input(user_input):
        print("Invalid input. Please enter rock, paper, or scissors.")
        continue

    # Generating computer's choice
    computer_choice = generate_computer_choice()

    # Applying game rules and determining the winner
    winner = get_winner(user_input.lower(), computer_choice)

    # Printing the results
    print("Your choice:", user_input)
    print("Computer's choice:", computer_choice)
    print(winner)

    # Asking if the user wants to play again
    play_again = input("Do you want to play again? (yes/no): ")
    if play_again.lower() != "yes":
        break
