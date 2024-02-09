import turtle
from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("White")
        self.hideturtle()
        self.penup()
        self.goto(0, 220)
        with open("score.txt") as score:
            self.high = int(score.read())
        self.write(f"Score:{self.score} Highscore:{self.high}", False, "center", ("Arial", 15, "normal"))

    def add(self):
        self.score += 1
        self.clear()
        self.write(f"Score:{self.score} Highscore:{self.high}", False, "center", ("Arial", 15, "normal"))

    def update(self):
        if self.score > self.high:
            self.high = self.score
        self.score = 0
        with open("score.txt", mode="w") as score:
            score.write(f"{self.high}")
        self.score
        self.clear()
        self.write(f"Score:{self.score} Highscore:{self.high}", False, "center", ("Arial", 15, "normal"))

    def gameover(self):
        self.goto(0, 0)
        self.write("Game Over", False, "center", ("Arial", 15, "normal"))
