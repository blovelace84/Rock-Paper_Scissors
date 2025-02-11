import random

#Initialize Scores
user_score = 0
computer_score = 0

choices = ['rock', 'paper', 'scissors']

def get_computer_choice():
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    global user_score, computer_score
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        user_score += 1
        return "You win!"
    else:
        computer_score += 1
        return "Computer wins!"

print("Let's play Rock, Paper, Scissors...")
print("Type 'exit' to exit the game. \n")
while True:
        #User input
        user_choice = input("Enter your choice: ").lower()

        if user_choice == 'exit':
            print("Final Score -> You {}, computer: {}".format(user_score, computer_score))
            print("Thanks for playing!")
            break
        if user_choice not in choices:
            print("Invalid choice. Please try again.")
            continue

        #computer choice
        computer_choice = get_computer_choice()
        print(f"Computer choice: {computer_choice}")

        #Determine Winner
        result = determine_winner(user_choice, computer_choice)
        print(result)
        print(f"Score -> You: {user_score}, Computer: {computer_score}\n")
