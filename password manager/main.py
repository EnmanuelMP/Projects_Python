from tkinter import *
from tkinter import messagebox
from pwd_generator import create_password
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_pwd():
    pwd = create_password()
    txt_3.delete(0,END)
    txt_3.insert(0, pwd)

# ---------------------------- FIND PASSWORD ------------------------------- #

def find_password():
    website = txt_1.get()

    try:
        with open("data.json", "r") as f:
            data:dict = json.load(f)

    except FileNotFoundError:
        messagebox.showinfo(
        title="Oops!", 
        message=f"You haven't saved any password!")
        return

    else:
        if website in data:
            pwd = data[website]["password"]
            email = data[website]["email"]

            txt_2.delete(0,END)
            txt_3.delete(0,END)

            txt_2.insert(0, email)
            txt_3.insert(0, pwd)
        
        else:
            messagebox.showinfo(
            title="Oops!", 
            message=f"Password not found.")



# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = txt_1.get()
    email = txt_2.get()
    password = txt_3.get()

    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if "" in [website, email, password]:
        messagebox.showinfo(
        title="Oops!", 
        message=f"Please don't leave any fields empty!")
        return

    is_ok = messagebox.askokcancel(
        title=website, 
        message=f"These are the details entered: \nEmail: {email}\nPassword: {password}\nIs it ok to save?")

    if is_ok:
        try:
            with open("data.json", "r") as f:
                data:dict = json.load(f)

        except FileNotFoundError:
            with open("data.json", "w") as f:
                json.dump(new_data, f, indent=4)

        else:
            data.update(new_data)

            with open("data.json", "w") as f:
                json.dump(data, f, indent=4)

        finally:
            txt_1.delete(0,END)
            txt_2.delete(0,END)
            txt_2.insert(0, "example@example.com")
            txt_3.delete(0,END)
        
# ---------------------------- UI SETUP ------------------------------- #

Window = Tk()
Window.title("Password Manager")
Window.config(padx=50, pady=50, bg="White")

canvas = Canvas(width=200,height=200, bg="White")
logo_img = PhotoImage(file=r"logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1, sticky="W", columnspan=2)

lbl_1= Label(text="Website:",bg="White")
lbl_1.grid(row=1,column=0, sticky="E")

lbl_2= Label(text="Email/Username:", bg="White")
lbl_2.grid(row=2,column=0, sticky="E")

lbl_3= Label(text="Password:", bg="White")
lbl_3.grid(row=3,column=0, sticky="E")

txt_1 = Entry(width=21)
txt_1.grid(row=1,column=1, columnspan=2, sticky="W")
txt_1.focus()

txt_2 = Entry(width=35)
txt_2.grid(row=2,column=1, columnspan=2, sticky="W")
txt_2.insert(0, "example@example.com")

txt_3 = Entry(width=21)
txt_3.grid(row=3,column=1, sticky="W")

btn_1 = Button(text="Generate Password", bg="White", command=generate_pwd)
btn_1.grid(row=3,column=2, sticky="W")

btn_2 = Button(text="Add", width=36, bg="White", command=save)
btn_2.grid(row=4,column=1, columnspan=2, sticky="W")

btn_3 = Button(text="search", bg="White", width=14, command=find_password)
btn_3.grid(row=1,column=2, sticky="W")

Window.mainloop()