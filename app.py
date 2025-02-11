from flask import Flask, render_template, request
import random

app = Flask(__name__)

# Possible choices
choices = ["rock", "paper", "scissors"]

# Determine winner function
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        return "You win!"
    else:
        return "Computer wins!"

@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    computer_choice = None
    if request.method == "POST":
        user_choice = request.form["choice"]
        computer_choice = random.choice(choices)
        result = determine_winner(user_choice, computer_choice)
    return render_template("index.html", result=result, computer_choice=computer_choice)

if __name__ == "__main__":
    app.run(debug=True)
