import time
import turtle


class snake:
    def __init__(self):
        self.snakes = []
        self.create()
        self.screen = turtle.Screen()

    def create(self):
        for i in range(5):
            snake = turtle.Turtle()
            snake.color("white")
            snake.shape("square")
            snake.penup()
            snake.goto(-1 * i * 20, 0)
            self.snakes.append(snake)

    def add(self):
        snake = turtle.Turtle()
        snake.color("white")
        snake.shape("square")
        snake.penup()
        snake.goto(self.snakes[- 1].pos())
        self.snakes.append(snake)

    def reset(self):
        for snake in self.snakes:
            snake.goto(1000, 1000)
        self.snakes.clear()
        self.create()

    def up(self):
        if not self.snakes[0].heading == 270.0:
            print(self.snakes[0].heading)
            self.snakes[0].setheading(90)

    def l(self):
        if not self.snakes[0].heading == 90.0:
            self.snakes[0].setheading(180)

    def r(self):
        if not self.snakes[0].heading == 180.0:
            self.snakes[0].setheading(0)

    def d(self):
        if not self.snakes[0].heading == 90.0:
            self.snakes[0].setheading(270)

    def move(self):

        for i in range(len(self.snakes) - 1, 0, -1):
            self.snakes[i].goto(self.snakes[i - 1].pos())
        self.snakes[0].forward(10)
        self.screen.listen()
        self.screen.onkeypress(self.up, "w")
        self.screen.onkeypress(self.l, "a")
        self.screen.onkeypress(self.r, "d")
        self.screen.onkeypress(self.d, "s")
