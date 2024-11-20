import turtle
import random

tim = turtle.Turtle()
tim.shape("arrow")

def shapes():
    for sides in range(3, 11):
        color = random.choice(["red", "green", "blue", "purple", "orange", "yellow", "pink", "brown", "cyan"])
        tim.pencolor(color)
        angle = 360 / sides
        for _ in range(sides):
            tim.forward(100)
            tim.right(angle)


shapes()

screen = turtle.Screen()
screen.exitonclick()