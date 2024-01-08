import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.all_car = []
        self.speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        randon_speed = random.randint(1,6)
        if randon_speed == 1:
            new_car = Turtle()
            new_car.shape("square")
            new_car.penup()
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.color(random.choice(COLORS))
            new_y = random.randint(-250, 250)
            new_car.goto(300, new_y)
            self.all_car.append(new_car)

    def car_move(self):
        for car in self.all_car:
            car.backward(self.speed)

    def inc_speed(self):
        self.speed += MOVE_INCREMENT






