
import random
print("Rock Paper Scissor Game")

choices = ["rock", "paper", "scissor"]
computerscore = 0
userscore = 0

while True:
    userinput = input("Enter a choice (rock/paper/scissor): ").lower()

    if userinput not in choices:
        print("Invalid choice. Please choose rock, paper, or scissor.")
        continue 

    computerinput = random.choice(choices)

    print(f"Your Choice: {userinput}")
    print(f"Computer Choice: {computerinput}")

    if userinput == computerinput:
        print("It's a tie!")
    elif (userinput == "rock" and computerinput == "scissor") or \
         (userinput == "paper" and computerinput == "rock") or \
         (userinput == "scissor" and computerinput == "paper"):
        print("YOU WIN!")
        userscore += 1
    else:
        print("COMPUTER WINS!")
        computerscore += 1

    print(f"Your Score: {userscore}")
    print(f"Computer Score: {computerscore}")

    playagain = input("Do you want to play again? (yes/no): ").lower()
    if playagain == "no":
        print("Thanks for playing, BYE!")
        break 
