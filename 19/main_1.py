import turtle
from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(500, 400)

is_race_on = False
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win? Enter a color:")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []


b = -230
c = -80


for _ in range(len(colors)):
    x = Turtle(shape="turtle")
    x.penup()
    x.color(colors[_])
    x.teleport(b,c)
    c += 30
    all_turtles.append(x)

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:

        if turtle.xcor() > 210:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You Win! {winning_color}")
            else:
                print(f"You Lose! {winning_color}")
        rand_distance = random.randint(1, 10)
        turtle.forward(rand_distance)



screen.exitonclick()