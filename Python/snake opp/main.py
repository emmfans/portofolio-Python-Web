import random
import time
from turtle import Screen, Turtle
import lib
import food
import score

screen = Screen()
screen.setup(600, 500)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
food = food.Food()
snake = lib.snake()
score = score.Score()
i = 0.07
game = True
while game:
    snake.move()
    if snake.snakes[0].distance(food) < 15:
        score.add()
        snake.add()
        food.move()
        snake.move()
        if i > 0.02:
            i -= 0.003
    if snake.snakes[0].xcor() > 280 or snake.snakes[0].xcor() < -280 or snake.snakes[0].ycor() > 230 or snake.snakes[
        0].ycor() < -230:
        snake.reset()
        score.update()
    for segment in snake.snakes:
        if snake.snakes[0] == segment:
            pass
        elif snake.snakes[0].distance(segment) < 8:
            snake.reset()
            score.update()
    time.sleep(i)
    screen.update()

screen.exitonclick()
