import turtle as t
import random

tom = t.Turtle()
t.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b

tom.shape("arrow")
tom.pensize(1)
tom.speed("fastest")



distance = 100
amount = 500


def s():
    for _ in range(amount):
        tom.color(random_color())
        tom.circle(distance)
        tom.setheading(0)
        tom.penup()
        tom.forward(3)
        tom.pendown()
        tom.left(10 + _ * 10)
s()










screen = t.Screen()
screen.exitonclick()