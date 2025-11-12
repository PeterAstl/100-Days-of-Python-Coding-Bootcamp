from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.home()
        self.x = 3
        self.y = 3
        self.move_speed = 0.02

    def move(self):

        new_x = self.xcor() + self.x
        new_y = self.ycor() + self.y
        self.goto(new_x, new_y)

    def switch_t(self):
        self.y = (self.y *-1)
        self.move_speed *= 0.9

    def switch_b(self):
        self.x = (self.x *-1)
        self.move_speed *= 0.9

    def reset_position(self):
        self.home()
        self.switch_b()
        self.move_speed = 0.02