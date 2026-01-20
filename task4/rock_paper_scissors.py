import random

print("Welcome to Rock-Paper-Scissors Game")
print("Rules:")
print("Rock beats Scissors")
print("Scissors beats Paper")
print("Paper beats Rock")
print("----------------------------------")

user_score = 0
computer_score = 0

while True:
    user_choice = input("\nEnter rock / paper / scissors (or exit to stop): ").lower()

    if user_choice == "exit":
        print("\nGame Finished")
        print("Final Score:")
        print("You:", user_score)
        print("Computer:", computer_score)
        break

    if user_choice not in ["rock", "paper", "scissors"]:
        print("Invalid input. Try again.")
        continue

    computer_choice = random.choice(["rock", "paper", "scissors"])

    print("You chose:", user_choice)
    print("Computer chose:", computer_choice)

    if user_choice == computer_choice:
        print("Result: It's a Tie")

    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "scissors" and computer_choice == "paper") or
        (user_choice == "paper" and computer_choice == "rock")
    ):
        print("Result: You Win")
        user_score += 1

    else:
        print("Result: Computer Wins")
        computer_score += 1

    print("Score -> You:", user_score, "| Computer:", computer_score)
