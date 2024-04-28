from tkinter import *
from tkinter import messagebox
from pwd_generator import create_password

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_pwd():
    pwd = create_password()
    txt_3.delete(0,END)
    txt_3.insert(0, pwd)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = txt_1.get()
    email = txt_2.get()
    password = txt_3.get()

    if "" in [website, email, password]:
        messagebox.showinfo(
        title="Oops!", 
        message=f"Please don't leave any fields empty!")
        return

    is_ok = messagebox.askokcancel(
        title=website, 
        message=f"These are the details entered: \nEmail: {email}\nPassword: {password}\nIs it ok to save?")

    if is_ok:
        with open("data.txt", "a",newline='') as f:
            f.write(f"{txt_1.get()}|{txt_2.get()}|{txt_3.get()}\n")

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

txt_1 = Entry(width=35)
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

Window.mainloop()