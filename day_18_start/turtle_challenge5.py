import turtle as t
import random

turtle_obj = t.Turtle()
screen = t.Screen()
t.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    r_color = (r, g, b)
    return r_color


def draw_circle():
    #r = 20
    turtle_obj.color(random_color())
    turtle_obj.circle(50)



def make_circles(num):

    turtle_obj.speed('fastest')
    for i in range(360 // num):
        turtle_obj.setheading(turtle_obj.heading()+num)
        draw_circle()
    screen.exitonclick()


make_circles(5)


