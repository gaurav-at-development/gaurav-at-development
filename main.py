# rocks paper scissor
rock = "ROCCCKKKKKKKKKKKKKK"
paper = "paperrrrrrrrrrrrrr"
scissor = "scissorrrrrrrrrrr"

game_images = [rock, paper, scissor]
import random

user_choice = int(input("rocks = 0 , paper = 1 ,scissors = 2\n"))

if user_choice >= 3:
    print("give a valid input \n you will lose")
else:
    print(game_images[user_choice])
    computer = random.randint(0, 2)
    computer_choice = computer

    print(computer_choice)
    print(game_images[computer_choice])
    if computer_choice == 2 and user_choice == 0:
        print("you won")
    elif user_choice == 2 and computer_choice == 0:
        print("you lose")
    elif computer_choice < user_choice:
        print("you won")
    elif computer_choice == user_choice:
        print("its tie")
    else:
        print("you lose")


