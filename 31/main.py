BACKGROUND_COLOR = "#B1DDC6"

import pandas
from tkinter import *
import random
import time

try:
    data = pandas.read_csv("words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("french_words.csv")
    to_learn = original_data.to_dict("records")
    random.shuffle(to_learn)
else:
    to_learn = data.to_dict("records")

current_card = {}


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    canvas.itemconfig(canvas_image, image=card_front)
    current_card = random.choice(to_learn)
    canvas.itemconfig(title, text = "French", fill = "black")
    canvas.itemconfig(word, text=current_card["French"], fill = "black")
    flip_timer = window.after(3000, func=flip_card)

def flip_card():
    canvas.itemconfig(canvas_image, image=card_back)
    canvas.itemconfig(title, text="English", fill="white")
    canvas.itemconfig(word, text=current_card["English"], fill="white")

def knows():
    global data
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("words_to_learn.csv", index = False)
    next_card()


window = Tk()
window.title("Learning Cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

card_back = PhotoImage(file="card_back.png")
card_front = PhotoImage(file="card_front.png")
canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
canvas_image = canvas.create_image(400, 263, image=card_front)
title = canvas.create_text(400, 150, text= "", font=("Arial", 40, "italic"))
word = canvas.create_text(400, 263, text= "", font=("Arial", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

# label_t = Label(window, text="French", bg= "white", font=("Arial", 40, "italic"))
# label_t.place(x=400, y=150, anchor="center")
#
# label_b = Label(window, text="trouve", bg= "white", font=("Arial", 60, "bold"))
# label_b.place(x=400, y=263, anchor="center")

image_w = PhotoImage(file="wrong.png")
button_w = Button(image=image_w, highlightthickness=0, command=next_card)
button_w.grid (row=1, column=0)

image_r = PhotoImage(file="right.png")
button_r = Button(image=image_r, highlightthickness=0, command=knows)
button_r.grid (row=1, column=1)

next_card()


window.mainloop()