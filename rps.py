import random

def rockPaperScis():
    flag = True
    choices = ["rock", "paper", "scissors"]

    while(flag):
        num = random.randint(0,2)
        print(num)
        choice = input('Type rock, paper, or scissors. Or type q to quit')
        if choice == "rock":
            if choices[num] == "rock":
                print("Game Tied! Computer chose rock as well.")
            elif choices[num] == "paper":
                print("You Lose! Computer chose paper.")
            else:
                print("You Win! Computer chose scissors.")
        elif choice == "paper":
            if choices[num] == "rock":
                print("You Win! Computer chose rock.")
            elif choices[num] == "paper":
                print("Game Tied! Computer chose paper as well.")
            else:
                print("You Lose! Computer chose scissors.")
        elif choice == "scissors":
            if choices[num] == "rock":
                print("You Lose! Computer chose rock.")
            elif choices[num] == "paper":
                print("You Win! Computer chose paper.")
            else:
                print("Game Tied! Computer chose scissors as well.")
        elif choice == "q":
            flag = False
            print("Thank you for playing.")
        else:
            print("Invalid Input.")

rockPaperScis()
