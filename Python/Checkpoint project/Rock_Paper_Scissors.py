import random   

print("Welcome to the Rock, Paper, Scissors Game")
print("Rules: \nRock beats Scissors \nScissors beats Paper \nPaper beats Rock")
print (" Rock")
print (" Paper")
print (" Scissors")
player1 = input("Enter your choice: rock, paper or scissors: ").lower()
computer = random.randint(1,3)

choices = {1: "rock", 2: "paper", 3: "scissors"}

print("Computer chose: ", choices[computer])
print("You chose: ", player1)

if player1 not in choices.values():
    print("Invalid input! You have not entered rock, paper or scissors, try again.")
else:
    if player1 == choices[computer]:
        print("It's a Draw!")
    else:
        if player1 == "rock":
            if choices[computer] == "paper":
                print("You lose!")
            else:
                print("You win!")
        elif player1 == "paper":
            if choices[computer] == "scissors":
                print("You lose!")
            else:
                print("You win!")
        elif player1 == "scissors":
            if choices[computer] == "rock":
                print("You lose!")
            else:
                print("You win!")

