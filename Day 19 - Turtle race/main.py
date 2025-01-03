from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500,height=400)

user_bet = screen.textinput(title= 'Make a bet', prompt = 'Which turtle will win the race? Enter a color: ')
colors = ['red','orange','yellow','green','blue','purple']

turtles = []

for color in colors:
    new_turtle = Turtle(shape='turtle')
    new_turtle.penup()
    new_turtle.color(color)
    new_turtle.goto(-230, 70 + colors.index(color) * -30)
    turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f'You have won! The {winning_color} turtle is the winner!')
            else:
                print (f'You have lost! The {winning_color} turtle is the winner!')

    
        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance)


screen.exitonclick()
