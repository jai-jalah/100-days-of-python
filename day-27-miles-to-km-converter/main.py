from tkinter import *


def miles_to_km():
    miles_to_km_calc = round(int(input.get()) * 1.609344)
    conversion.config(text=miles_to_km_calc)


window = Tk()
window.title("Miles to Km Converter")
window.config(padx=20, pady=20)

equal_to = Label(text="==")
equal_to.grid(column=0, row=1)

miles = Label(text="Miles")
miles.grid(column=2, row=0)

km = Label(text="Km")
km.grid(column=2, row=1)

conversion = Label(text=0)
conversion.grid(column=1, row=1)

button = Button(text="Calculate", command=miles_to_km)
button.grid(column=1, row=2)

input = Entry(width=10)
input.grid(column=1, row=0)

window.mainloop()