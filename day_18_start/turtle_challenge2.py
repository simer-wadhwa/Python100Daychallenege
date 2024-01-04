from turtle import Turtle

tt_turtle_obj = Turtle()

for _ in range(15):
    tt_turtle_obj.forward(10)
    tt_turtle_obj.penup()
    tt_turtle_obj.forward(10)
    tt_turtle_obj.pendown()