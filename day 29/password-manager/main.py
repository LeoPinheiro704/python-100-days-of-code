from tkinter import * 
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
  letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
  numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
  symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

  password_letters = [choice(letters) for _ in range(randint(8, 10))]
  password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
  password_symbols = [choice(symbols) for _ in range(randint(2, 4))]

  password_list = password_letters + password_symbols + password_numbers
  shuffle(password_list)

  password = "".join(password_list)
  password_input.delete(0, END)
  password_input.insert(0, password)
  pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
  website = website_input.get()
  email = email_input.get()
  password = password_input.get()
  
  if len(website) == 0 or len(password) == 0:
    messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
  else: 
    is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \n"
                          f"Email: {email}\nPassword: {password}\nIs it ok to save?")
    if is_ok:
      with open("data.txt", mode="a") as data_file:
        content = f"{website} | {email} | {password}\n"
        data_file.write(content)
        website_input.delete(0, END)
        password_input.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
padlock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=padlock_img)
canvas.grid(column=1, row=0)


website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3,)

website_input = Entry(width=35)
website_input.grid(column=1, row=1, columnspan=2, sticky='w')
website_input.focus()

email_input = Entry(width=35)
email_input.grid(column=1, row=2, columnspan=2, sticky='w')
email_input.insert(0, "email@gmail.com")

password_input = Entry(width=21)
password_input.grid(column=1, row=3, sticky='w')

generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(column=2, row=3, sticky='w')

add_button = Button(text="Add", width=36, command=save_password)
add_button.grid(column=1, row=4, columnspan=2, sticky='w')

window.mainloop()