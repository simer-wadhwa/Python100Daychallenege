from turtle import Turtle
import random

turtle = Turtle()

colours =["MediumSlateBlue", "plum", "pink", "linen", "Red",
          "LightGoldenrodYellow", "Cyan", "Firebrick"]

directions = [0, 90, 180, 270]

turtle.speed('slowest')
turtle.pensize(15)

for _ in range(100):
    turtle.color(random.choice(colours))
    turtle.forward(30)
    turtle.setheading(random.choice(directions))






