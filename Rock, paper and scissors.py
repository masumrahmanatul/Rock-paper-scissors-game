import random

exit = False
user_points = 0
computer_points = 0


while exit == False and (computer_points < 6 or user_points < 6):
    options = ["rock", "paper", "scissors"]
    user_input = input("Rock, paper, scissors or exit?: ")
    computer_input = random.choice(options)

    if user_input.lower() == 'exit':
        print("Program ended")
        exit = True

    elif user_input.lower() == computer_input:
        print("Computer:",computer_input)
        print("Player:",user_input)
        print("It's a tie")
        print("Player score:", user_points, "||", "Computer score:", computer_points)
        print("")

    elif user_input.lower() == 'rock':
        if computer_input == 'paper':
            print("Computer:",computer_input)
            print("Player:",user_input)
            print("Computer wins this round!")
            computer_points += 1
            print("Player score:",user_points,"||","Computer score:",computer_points)
            print("")
        elif computer_input == 'scissors':
            print("Computer:",computer_input)
            print("Player:",user_input)
            print("Player wins this round!")
            user_points += 1
            print("Player score:", user_points, "||", "Computer score:", computer_points)
            print("")

    elif user_input.lower() == 'paper':
        if computer_input == 'rock':
            print("Computer:",computer_input)
            print("Player:",user_input)
            print("Player wins this round!")
            user_points += 1
            print("Player score:", user_points, "||", "Computer score:", computer_points)
            print("")
        elif computer_input == 'scissors':
            print("Computer:",computer_input)
            print("Player:",user_input)
            print("Computer wins this round!")
            computer_points += 1
            print("Player score:", user_points, "||", "Computer score:", computer_points)
            print("")

    elif user_input.lower() == 'scissors':
        if computer_input == 'paper':
            print("Computer:",computer_input)
            print("Player:",user_input)
            print("Player wins this round!")
            user_points += 1
            print("Player score:", user_points, "||", "Computer score:", computer_points)
            print("")
        elif computer_input == 'rock':
            print("Computer:",computer_input)
            print("Player:",user_input)
            print("Computer wins this round!")
            computer_points += 1
            print("Player score:", user_points, "||", "Computer score:", computer_points)
            print("")
            
    if computer_points == 6:
        print("COMPUTER WINS THE GAME!")
        break
    elif user_points == 6:
        print("PLAYER WINS THE GAME!!")
        break
