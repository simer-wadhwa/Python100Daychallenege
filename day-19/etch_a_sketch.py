from turtle import Turtle, Screen

turtle = Turtle()
screen = Screen()


def move_forward():
    turtle.forward(10)


def move_backward():
    turtle.backward(10)


def clockwise():
    turtle.right(10)


def anticlockwise():
    turtle.left(10)


def clear_screen():
    turtle.clear()
    turtle.penup()
    turtle.home()
    turtle.pendown()


screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=clockwise)
screen.onkey(key="d", fun=anticlockwise)
screen.onkey(key="c", fun=clear_screen)
screen.exitonclick()


