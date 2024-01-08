import random
import time
from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball


screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("My Ping Pong Game")
screen.tracer(0)


paddle_left = Paddle((-350, 0))
paddle_right = Paddle((350, 0))
ball = Ball()






screen.listen()
screen.onkeypress(paddle_left.go_up, "Up")
screen.onkeypress(paddle_left.go_down, "Down")
screen.onkeypress(paddle_right.go_up, "w")
screen.onkeypress(paddle_right.go_down, "s")

is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.1)
    ball.move()

    # Detect collision with wall
    if ball.ycor() < -280 or ball.ycor() > 280:
        ball.bounce_y()

    # Detect collision with wall
    if ball.distance(paddle_left) < 50 and ball.xcor() < -320 or ball.distance(paddle_right) < 50 and ball.xcor() > 320:
        ball.bounce_x()










screen.exitonclick()
