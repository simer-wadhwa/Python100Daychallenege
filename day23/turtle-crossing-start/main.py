import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

player = Player()
car = CarManager()
score = Scoreboard()

screen.onkey(player.move, "Up")
game_is_on = True
new_speed = 0
while game_is_on:
    time.sleep(0.1)
    screen.update()
    # Detect with car
    for cars in car.all_car:
        if cars.distance(player) < 20:
            score.game_over()
            game_is_on = False

    # Detect player reached other side

    if player.is_at_finish_line():
        score.increase_score()
        player .refresh()
        car.inc_speed()

    car.create_car()
    car.car_move()


screen.exitonclick()
