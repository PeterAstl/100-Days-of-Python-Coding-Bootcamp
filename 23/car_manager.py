import random
import time
from turtle import Turtle


COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5

class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color(random.choice(COLORS))
        self.penup()
        self.shapesize(1, 2)
        self.goto(280, random.randint(-230, 270))
        self.setheading(180)
        self.speed("fastest")
        self.move_distance = STARTING_MOVE_DISTANCE

    def move(self, y):
        self.forward(self.move_distance + y)



