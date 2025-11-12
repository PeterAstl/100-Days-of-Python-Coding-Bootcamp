
from tkinter import *

def button_clicked():
    new_text = input.get()
    my_label.config(text=new_text)

window = Tk()
window.title("My First GUI")
window.minsize(500, 500)
window.config(padx=100,pady=200)

my_label = Label(text="Hello World", font=("Arial", 20, "bold"), fg="blue")
# my_label.pack()
# my_label.place(x=200, y=200)
my_label.grid(column=0, row=0)

button = Button(window, text="Click Me", command= button_clicked )
button.grid(column=1, row=1)

button_1 = Button(window, text="Click Me", command= button_clicked )
button_1.grid(column=2, row=0)

input = Entry(window)
input.grid(column=3, row=2)


window.mainloop()