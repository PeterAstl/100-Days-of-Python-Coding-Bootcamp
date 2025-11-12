
from turtle import Turtle,Screen
from paddle import Paddle
from ball import Ball
from score import Score
import time

screen= Screen()
screen.bgcolor("black")
screen.setup(width=800,height=600)
screen.title("PINGPONG")
screen.tracer(0)

paddle1= Paddle((350,0))
paddle2= Paddle((-350,0))

ball= Ball()

score = Score()

screen.listen()
screen.onkeypress(paddle1.go_up, "Up")
screen.onkeypress(paddle1.go_down, "Down")
screen.onkeypress(paddle2.go_up, "w")
screen.onkeypress(paddle2.go_down, "s")


game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.switch_t()

    if ball.xcor() < -330 and ball.distance(paddle2) < 50 or ball.distance(paddle1) < 50 and ball.xcor() > 330:
        ball.switch_b()

    if ball.xcor() < -380:
        ball.reset_position()
        score.score_l()

    if ball.xcor() > 380:
        ball.reset_position()
        score.score_r()

screen.exitonclick()
