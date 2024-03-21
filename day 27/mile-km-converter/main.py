from tkinter import *


def converter():
  mile = float(input.get())
  km = round(mile * 1.609344)
  result_label.config(text=f"{km}")
  

window = Tk()
window.title("Miles to Km Converter")
window.config(padx=20, pady=20)


input = Entry(width=10)
input.insert(index=0, string="0")
input.grid(column=1, row=0)


miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)


km_label = Label(text="Km")
km_label.grid(column=2, row=1)


equal_label = Label(text="is equal to")
equal_label.grid(column=0, row=1)


result_label = Label(text=0)
result_label.grid(column=1, row=1)


button = Button(text="Calculate", command=converter)
button.grid(column=1, row=2)


window.mainloop()