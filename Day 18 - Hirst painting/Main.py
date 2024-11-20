'''
import colorgram

colors = colorgram.extract('hirst.jpg', 200)

rgb_tuples = [(color.rgb.r, color.rgb.g, color.rgb.b) for color in colors]

print(rgb_tuples)
'''

import turtle
import random
art = turtle.Turtle()
turtle.colormode(255)

art.penup()
art.setx(-200)
art.sety(-200)
art.hideturtle()
art.speed("fastest")


color_list = [(245, 243, 238), (240, 246, 241), (246, 242, 244), (201, 166, 109), (235, 239, 243),
 (146, 77, 53), (166, 153, 43), (52, 94, 126), (138, 30, 20), (217, 202, 144), (132, 163, 183),
 (47, 120, 87), (196, 93, 74), (16, 101, 70), (69, 50, 41), (159, 145, 158), (232, 177, 164),
 (183, 206, 172), (102, 74, 77), (135, 172, 155), (87, 145, 126), (157, 14, 17), (39, 65, 80),
 (66, 64, 60), (34, 72, 90), (213, 180, 183), (177, 197, 204), (111, 128, 148), (111, 136, 139),
 (172, 104, 105), (176, 193, 208), (28, 72, 55), (38, 64, 91), (99, 27, 28)]


def draw_art():
  for row in range(10): # 10 rows
    for _ in range(10): #10 dots per row
       art.color(random.choice(color_list))
       art.dot(20)
       art.penup()
       art.forward(50)
       art.pendown()

    # Move to the next row
    art.penup()
    art.setx(-200)  # Return to the left side
    art.sety(art.ycor() + 50)  # Move up for the next row
    art.pendown()

draw_art()


screen = turtle.Screen()
screen.exitonclick()
