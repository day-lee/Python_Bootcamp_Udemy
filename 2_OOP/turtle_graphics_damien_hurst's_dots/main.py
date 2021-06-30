import colorgram
from turtle import Turtle, Screen
import random
import turtle
'''
colors = colorgram.extract('colordots.jpg', 10)
#can use any image of your choice

rgb_colors = []
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b

    new_color = (r, g, b)
    rgb_colors.append(new_color)
    # rgb = color.rg
    # rgb_colors.append(rgb)

print(rgb_colors)
color_list = [(202, 216, 243), (138, 165, 199), (216, 147, 109), (30, 39, 60), (205, 135, 143), (52, 107, 153), (140, 182, 165)]
#most frequently used colours in the image file

'''
# first_color = colors[0]
# rgb = first_color.rgb
# print(rgb)

tur = Turtle()

# tur.shape("circle")
# tur.speed(5)
# tur.dot(20, "blue")
# tur.color("blue")
# tur.stamp()
# tur.forward(120)
color_list = [(202, 216, 243), (138, 165, 199), (216, 147, 109), (30, 39, 60), (205, 135, 143), (52, 107, 153), (140, 182, 165)]
#most frequently used colours in the image file


turtle.colormode(255)

def random_color():
    num = random.randint(0, 6)
    color = color_list[num]
    return color

def dots():
    for dot in range(10):
        tur.pencolor(random_color())
        tur.dot(20)
        tur.penup()
        tur.fd(50)

tur.shape("turtle")
tur.penup()
i = -200
for dot in range(10):
    tur.setposition(-200, i)
    dots()
    i += 50

tur.hideturtle()
screen = Screen()
screen.exitonclick()
