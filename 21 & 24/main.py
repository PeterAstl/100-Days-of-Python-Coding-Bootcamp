
from turtle import Screen

from score import Score
from snake import Snake
from food import Food
import time


screen = Screen()
screen.setup(width=800, height=800)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()

screen.listen()
screen.onkeypress(snake.up, "w")
screen.onkeypress(snake.down, "s")
screen.onkeypress(snake.left, "a")
screen.onkeypress(snake.right, "d")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.05)
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        score.add()
        snake.extend()

    if snake.head.xcor() > 380 or snake.head.xcor() < -380 or snake.head.ycor() > 380 or snake.head.ycor() < -380:
        score.reset()
        snake.reset_snake()

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            score.reset()
            snake.reset_snake()



screen.exitonclick()