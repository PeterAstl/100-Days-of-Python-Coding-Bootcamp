import math
from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #

def reset():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    label.config(text="Timer")
    label_2.config (text="")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def button_start():
    global reps
    global label
    reps += 1
    if reps % 8 == 0:
        count_down(LONG_BREAK_MIN)
        label.config(text = "++ Break", fg=RED)
    elif reps % 2 == 0:
        count_down(SHORT_BREAK_MIN)
        label.config(text="Break", fg=PINK)
    else:
        count_down(WORK_MIN)
        label.config(text="Work", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count):
    global reps
    global label_2
    global timer
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    if count > 0:
        canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
        timer = window.after(1000, count_down, count -1)

    else:
        button_start()
        new_text = "✅" * math.floor((reps / 2))
        label_2.config(text=new_text)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

label = Label(text = "Timer", fg=GREEN, bg=YELLOW, font= (FONT_NAME, 50, "normal"))
label.grid(column = 0, row = 0)
label.grid(column = 1, row = 0)

label_2 = Label(fg=GREEN, bg=YELLOW, font= (FONT_NAME, 10, "bold"))
label_2.grid(column = 1, row = 3)


button_1 = Button(text= "Start", command=button_start)
button_1.grid(column=0, row=2)
button_2 = Button(text = "Reset", command = reset)
button_2.grid(column=2, row=2)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato)
timer_text = canvas.create_text(100,130, text="00:00", fill= "white", font = (FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)



window.mainloop()