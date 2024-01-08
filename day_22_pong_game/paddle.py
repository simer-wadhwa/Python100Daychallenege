from turtle import Turtle



class Paddle:
    def __init__(self, position):
        self.paddle = Turtle(shape="square")
        self.create_paddle(position)


    def create_paddle(self, position):
        self.paddle.penup()
        self.paddle.color("white")
        self.paddle.shapesize(stretch_wid=5, stretch_len=1)
        self.paddle.goto(position)

    def go_up(self):
        new_y = self.paddle.ycor() + 20
        self.paddle.goto(self.paddle.xcor(), new_y)

    def go_down(self):
        new_y = self.paddle.ycor() - 20
        self.paddle.goto(self.paddle.xcor(), new_y)

