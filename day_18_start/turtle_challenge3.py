from turtle import Turtle
import random

turtle = Turtle()

colours =["MediumSlateBlue", "plum", "pink", "linen", "Red",
          "LightGoldenrodYellow", "Cyan", "Firebrick"]


def draw_shapes(shape_size):
    angle = 360/shape_size
    for _ in range(shape_size):
        turtle.forward(100)
        turtle.right(angle)




for shape in range(3, 11):
    turtle.color(random.choice(colours))
    draw_shapes(shape)



#ameature code
# #triangle
# for _ in range(3):
#     turtle.forward(100)
#     turtle.right(120)
#
#
# #square
#
# for _ in range(4):
#     turtle.forward(100)
#     turtle.right(90)
#
#
# #pentagon
#
# for _ in range(5):
#     turtle.forward(100)
#     turtle.right(72)
#
#
# #hexagon
#
# for _ in range(6):
#     turtle.forward(100)
#     turtle.right(60)
#
# #heptagon
# for _ in range(7):
#     turtle.forward(100)
#     turtle.right(52)
#
# #octagon
# for _ in range(8):
#     turtle.forward(100)
#     turtle.right(45)
#
# #nanogon
# for _ in range(9):
#     turtle.forward(100)
#     turtle.right(40)
#
# #decagon
# for _ in range(10):
#     turtle.forward(100)
#     turtle.right(36)