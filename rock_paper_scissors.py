import random

choices = ["rock", "paper", "scissors"]

user_score = 0
computer_score = 0

print("ROCK PAPER SCISSORS GAME")

while True:
    user = input("\nEnter rock, paper or scissors: ").lower()

    if user not in choices:
        print("Invalid choice ,Please try again.")
        continue

    computer = random.choice(choices)

    print("You chose:", user)
    print("Computer chose:", computer)

    if user == computer:
        print("It's a tie")

    elif user == "rock" and computer == "scissors":
        print("You win")
        user_score += 1

    elif user == "paper" and computer == "rock":
        print("You win")
        user_score += 1

    elif user == "scissors" and computer == "paper":
        print("You win")
        user_score += 1

    else:
        print("Computer wins")
        computer_score += 1

    print("Your score:", user_score)
    print("Computer score:", computer_score)

    play_again = input("\nDo you want to play again? (yes/no): ").lower()

    if play_again = "yes":
        break

print("\n FINAL SCORE ")
print("Your score:", user_score)
print("Computer score:", computer_score)

if user_score > computer_score:
    print("You won the game")

elif computer_score > user_score:
    print("Computer won the game")

else:
    print("The game is a tie")
