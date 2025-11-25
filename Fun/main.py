import os
from turtle import Screen, Turtle
from tkinter import *
from tkinter.filedialog import askopenfilename
from PIL import Image, ImageTk

screen = Screen()
screen.setup(width=800, height=800)

canvas = screen.getcanvas()
bg_image_ref = None

tom = Turtle()
tim = Turtle()
tim.penup()
tim.shape("square")
tim.color("red")
tim.speed("fastest")
tim.goto(300,300)
tom.penup()
tom.color('black')
tom.shape('square')
tom.speed("fastest")



def forward():
    tom.setheading(90)
    tom.forward(100)
def backward():
    tom.setheading(270)
    tom.forward(100)
def left():
    tom.setheading(180)
    tom.forward(100)
def right():
    tom.setheading(0)
    tom.forward(100)

def check():
    global bg_image_ref
    if tom.distance(300,300) <= 5:
            file_path = askopenfilename(title="Select a file")
            size_bytes = os.path.getsize(file_path)
            size_mb = round(size_bytes / (1024 ** 2), 1)
            print(f"{size_mb} mb")

            if file_path.endswith(".png") or file_path.endswith(".jpg") or file_path.endswith(".jpeg"):
                img = Image.open(file_path)
                img = img.resize((800, 800), Image.Resampling.LANCZOS)
                bg_image_ref = ImageTk.PhotoImage(img)
                x = canvas.create_image(0,0, image=bg_image_ref, anchor="center")
                print(x)


screen.listen()
screen.onkey(forward, 'w')
screen.onkey(backward, 's')
screen.onkey(left, 'a')
screen.onkey(right, 'd')
screen.onkey(check, "e")



screen.exitonclick()
