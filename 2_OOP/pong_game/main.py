from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
import time
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width= 800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0) #turn off the animation


r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = ScoreBoard()


screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")


game_is_on = True
while game_is_on:
    scoreboard.front_page()
    scoreboard.name()
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()


    #Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    #Detect collision with both paddle
    if ball.distance(r_paddle) < 40 and ball.xcor() > 330 or ball.distance(l_paddle) < 40 and ball.xcor() < -330:
        time.sleep(0.05)
        ball.bounce_x()

    #Detect when paddle misses the ball
    if ball.xcor() > 370:
        ball.reset_position()
        scoreboard.l_point()

    if ball.xcor() < -370:
        ball.reset_position()
        scoreboard.r_point()

    #rule: 3 point lead wins the game
    if scoreboard.r_score == 3:
        game_is_on = False
        scoreboard.finish("B")

    elif scoreboard.l_score == 3:
        game_is_on = False
        scoreboard.finish("A")

screen.exitonclick()