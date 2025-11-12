import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
player = Player()
car_manager_l = []
scoreboard = Scoreboard()

screen.setup(width=600, height=600)
screen.title("Turtle Crossing")
screen.tracer(0)
x = 0
y = 0
z = 7

screen.listen()
screen.onkeypress(player.move, "w")


game_is_on = True
while game_is_on:
    if z == 0:
        car_manager_l = ""
    if x % z == 0:
        car_manager = CarManager()
        car_manager_l.append(car_manager)

    x += 1
    time.sleep(0.1)
    screen.update()
    for car in car_manager_l:
        car.move(y)

    if player.ycor() > 270:
        y += 5
        z -= 1
        scoreboard.update()
        player.refresh()

    for car in car_manager_l:
        if player.distance(car) < 20:
            scoreboard.refresh()
            player.refresh()
            x = 0
            y = 0
            z = 7


screen.exitonclick()