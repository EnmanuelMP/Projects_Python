from tkinter import *
from tkinter.font import Font
def miles_to_km():
    miles = float(miles_input.get())
    km = round(miles * 1.689)
    kilometer_result_label.config(text=f"{km}")


window = Tk()
window.title("Miles to kilometer converter")
window.config(padx=20, pady=20, bg="#38383A")

miles_input = Entry(width=10)
miles_input.grid(column=1, row=0)

bold_font = Font(family="Helvetica", size=10, weight="bold")

miles_label = Label(text="Miles",padx=5, bg="#38383A", foreground="White", font=bold_font)
miles_label.grid(column=2,row=0)

is_equal_label = Label(text="is equal to", bg="#38383A", foreground="White", font=bold_font)
is_equal_label.grid(column=0,row=1)

kilometer_result_label = Label(text="0", bg="#38383A", foreground="White", font=bold_font)
kilometer_result_label.grid(column=1, row=1)

kilometer_label = Label(text="km", bg="#38383A", foreground="White", font=bold_font)
kilometer_label.grid(column=2, row=1)

btn = Button(text="Convert", command=miles_to_km)
btn.grid(column=1,row=2)


window.mainloop()