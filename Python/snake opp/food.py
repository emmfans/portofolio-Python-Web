from turtle import Turtle
import random
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(0.5,0.5)
        self.color("white")
        x = random.randint(-230, 230)
        y = random.randint(-230, 230)
        self.goto(x,y)



    def move(self):
        x=random.randint(-230,230)
        y=random.randint(-230,230)
        self.goto(x,y)