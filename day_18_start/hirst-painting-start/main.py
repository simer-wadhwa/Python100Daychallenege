# ###This code will not work in repl.it as there is no access to the colorgram package here.###
# ##We talk about this in the video tutorials##
# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)

import turtle as t
import random


turtle_obj = t.Turtle()
turtle_obj.speed("fastest")
turtle_obj.penup()
turtle_obj.hideturtle()
color_list = [(202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]
t.colormode(255)
turtle_obj.goto(10, 10)

turtle_obj.setheading(225)
turtle_obj.forward(300)
turtle_obj.setheading(0)


def tendots(num):
    for dot in range(1, num+1):
        turtle_obj.dot(20, random.choice(color_list))
        turtle_obj.forward(50)

        if dot % 10 == 0:
            turtle_obj.setheading(90)
            turtle_obj.forward(50)
            turtle_obj.setheading(180)
            turtle_obj.forward(500)
            turtle_obj.setheading(0)

tendots(100)







    ##tendots()

    # turtle_obj.right(90)
    # turtle_obj.penup()
    # turtle_obj.forward(50)
    # turtle_obj.pendown()
    # turtle_obj.right(90)