from turtle import Turtle, Screen, color
import random

screen = Screen()
screen.setup(width=500, height=480)

user_bet = screen.textinput(title="Make your bet", prompt="which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []

is_race_on = True

for num in range(6):
    turtle = Turtle(shape="turtle") #Create Objects
    turtle.color(colors[num])
    turtle.penup()
    turtle.goto(x=-230, y=-150 + num*70)
    all_turtles.append(turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner.")
            else:
                print("you lose.")
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()
