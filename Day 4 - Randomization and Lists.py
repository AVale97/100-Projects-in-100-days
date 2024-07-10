rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random

options = ["rock","paper","scissors"]
computer = options[random.randint(0,2)]


game_images = [rock, paper, scissors]

choice = input("rock, paper or scissors?\n").lower()

if choice in options:
    choice_index = options.index(choice)
    print("You chose:")
    print(game_images[choice_index])

    print(f"Computer chose: {computer}")
    computer_index = options.index(computer)
    print(game_images[computer_index])

    if computer == choice:
        print ("You draw")
    elif (computer == "rock" and choice == "paper") or (computer == "paper" and choice ==           "scissors") or (computer == "scissors" and choice == "rock"):
        print ("You win!")
    else:
        print ("You lose")
else:
    print("Invalid play. Please choose rock, paper, or scissors.")
