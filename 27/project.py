from tkinter import *



def miles():
    new_text = float(input.get())
    x  = new_text * 1.609
    my_km_text.config(text=f"{x}")

window = Tk()
window.title("My First GUI")
window.minsize(500, 500)
window.config(padx=100,pady=200)

my_label = Label(text="Mile to Km Converter", font=("Arial", 20, "bold"))
my_label.grid(column=1, row=0)

my_miles = Label(text="Miles", font=("Arial", 20,))
my_miles.grid(column=2, row=1)

my_text = Label(text="is equal to", font=("Arial", 20,))
my_text.grid(column=0, row=2)

my_km_text = Label(text="0", font=("Arial", 20,))
my_km_text.grid(column=1, row=2)

my_km = Label(text="Km", font=("Arial", 20,))
my_km.grid(column=2, row=2)

button = Button(window, text="Click Me", command= miles)
button.grid(column=1, row=3)

input = Entry(window)
input.grid(column=1, row=1)


window.mainloop()