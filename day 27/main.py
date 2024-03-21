import tkinter


def button_clicked():
  my_label.config(text=input.get())
  print("clicked")


window = tkinter.Tk()
window.title("My first GUI Program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)


# Label
my_label = tkinter.Label(text="I am a label", font=("Arial", 24, "bold"))
my_label.config(text="New Text")
# my_label.place(x=0, y=0)
my_label.grid(column=0, row=0)


# Button
button = tkinter.Button(text="Click", command=button_clicked)
button2 = tkinter.Button(text="Click 2")
button.grid(column=1, row=1)
button2.grid(column=2, row=0)


# Entry
input = tkinter.Entry(width=10)
# input.pack()
input.grid(column=3, row=3)
print(input.get())








window.mainloop()
