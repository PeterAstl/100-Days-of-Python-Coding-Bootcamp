from tkinter import *
from tkinter import messagebox
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def shuffle_pw():
    password_letters = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_symbols = [random.choice(symbols) for _ in range(random.randint(2, 4))]
    password_numbers = [random.choice(numbers) for _ in range(random.randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers

    random.shuffle(password_list)

    pw = "".join(password_list)

    return pw

def password_creat():
    new = shuffle_pw()
    input_p.delete(0, END)
    input_p.insert(0, new)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
        web = input_w.get()
        mail = input_u.get()
        pw = input_p.get()
        new_data = {
            web: {
                "mail": mail,
                "pw": pw,
            }
        }

        if len(web) == 0 or len(mail) == 0 or len(pw) == 0:
            messagebox.showerror("Error", "Please fill all the fields")
        else:
            is_ok = messagebox.askokcancel(title = "Info", message = f"You want to save this information?\n {web} \n{mail}\n {pw}")
            if is_ok:
                try:
                    with open("passwords.json", "r") as data_file:
                        data = json.load(data_file)

                except FileNotFoundError:
                    with open("passwords.json", "w") as data_file:
                        json.dump(new_data, data_file, indent=4)

                else:
                    data.update(new_data)
                    with open("passwords.json", "w") as data_file:
                        json.dump(data, data_file, indent=4)
                finally:
                        input_p.delete(0, END)
                        input_w.delete(0, END)





def search():
    try:
        with open("passwords.json", "r") as data:
            data = json.load(data)
            info = data[input_w.get()]
            messagebox.showinfo("Your Website Data", f"{input_w.get()}\n{info["mail"]}\n{info["pw"]}")
    except FileNotFoundError, KeyError:
        messagebox.showerror("Error", "No Website saved with this name")


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pw Manager")
window.config(padx=40, pady=20)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

label_w = Label(text="Website:")
label_w.grid(row=1, column=0)

label_u = Label(text="Email/Username:")
label_u.grid(row=2, column=0)

label_pw = Label(text="Password:")
label_pw.grid(row=3, column=0)

input_w = Entry(width=51)
input_w.grid(column=1, row=1, columnspan=2)
input_w.focus()

input_u = Entry(width=51)
input_u.grid(column=1, row=2, columnspan=2)
input_u.insert(0, "astlpeter@gmail.com")

input_p = Entry(window, width=51)
input_p.grid(column=1, row=3, columnspan=2)

button = Button(text="Generate Password", command= password_creat)
button.grid(column=2, row=3)

button2 = Button(text="Add",width =44, command=save)
button2.grid(column=1, row=4, columnspan=2)

button_3 = Button(text="Search",width =14, command=search)
button_3.grid(column=2, row=1)

window.mainloop()