import turtle
import random


tim = turtle.Turtle()
turtle.colormode(255)
tim.shape("arrow")
tim.pensize(15)
directions = [0, 90, 180, 270]
tim.speed("fastest")

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return (r, g, b)

def walk():
    for _ in range(300):
        tim.pencolor(random_color())
        tim.forward(random.randint(10, 100))
        tim.setheading(random.choice(directions))


walk()

screen = turtle.Screen()
screen.exitonclick()