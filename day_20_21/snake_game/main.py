import time

from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard


# mycode
# x_distance = [0, -20, -40]
# turtle_line = []
#
# for turtle_index in range(3):
#     new_turtle = Turtle("square")
#     new_turtle.color("white")
#     new_turtle.setpos(x_distance[turtle_index], 0)
#     turtle_line.append(new_turtle)
#
# print(turtle_line)

screen = Screen()
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = ScoreBoard()


screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

is_game_on = True

while is_game_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        score.increase_score()
        snake.extend()

    # Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        is_game_on = False
        score.reset()

    # Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            is_game_on = False
            score.reset()


screen.exitonclick()
