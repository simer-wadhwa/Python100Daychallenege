from turtle import Turtle

ALIGNMENT = "left"
FONT = ("Arial", 22, "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.highscore = self.read_highscore()
        self.color("white")
        self.penup()
        self.goto(x=0, y=270)
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score :{self.highscore} ", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
        self.write_highscore()
        self.score = 0
        self.update_score()

    def write_highscore(self):
        with open("data.txt", mode="w") as file:
            file.write(f"{self.highscore}")

    def read_highscore(self):
        with open("data.txt", mode="r") as file:
            data = file.read()
        return int(data)

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_score()
