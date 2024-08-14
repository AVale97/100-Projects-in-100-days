import random

number = random.randint(1, 100)

#Requesting difficulty

print("Welcome to the guessing game!")
while True:
    difficulty = input('Choose a difficulty, type "easy" or "hard": ').lower()

    if difficulty == "easy":
        tries = 10
        break
    elif difficulty == "hard":
        tries = 5
        break
    else:
        print("Pick a valid difficulty")

#Defining number pick function
def pick_number():
    global tries
    while tries > 0:
        try:
            user_pick = int(input('Please choose a number from 1 to 100: '))
            if user_pick < 1 or user_pick > 100:
                print("Please choose a number within the range 1 to 100.")
                continue
        except ValueError:
            print("Invalid input. Please enter an integer.")
            continue

        if user_pick < number:
            print("Number is higher")
        elif user_pick > number:
            print("Number is lower")
        else:
            print("You won!")
            return
        tries -= 1
        print(f"Tries left: {tries}")
    else:
        print(f"You lost! The number was {number}")

pick_number()
