from turtle import Turtle


class State(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("black")

    def write_state(self,state, x, y):
        self.goto(x, y)
        self.write(f"{state}", align="center", font=("Arial", 10, "normal"))