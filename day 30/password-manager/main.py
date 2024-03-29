from tkinter import * 
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

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


# ---------------------------- SEARCH PASSWORD ------------------------------- #
def search():
  website = website_input.get()
  try:
    with open("data.json", mode="r") as data_file:
        data = json.load(data_file)
  except FileNotFoundError:
    messagebox.showinfo(title="Error", message="You do not have any password saved.")
  else:
    if website in data:
      email = data[website]["email"]
      password = data[website]["password"]
      messagebox.showinfo(title=f"{website}", message=f"Email: {email}\nPassword: {password}")
    else:
      messagebox.showinfo(title="Error", message=f"You do not have {website} password saved.")

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
  website = website_input.get()
  email = email_input.get()
  password = password_input.get()
  new_data = {
    website: {
      "email": email,
      "password": password
    }
  }
  
  if len(website) == 0 or len(password) == 0:
    messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
  else:
    try:
      with open("data.json", mode="r") as data_file:
        data = json.load(data_file)
    except FileNotFoundError:
      with open("data.json", mode="w") as data_file:
        json.dump(new_data, data_file, indent=4)
    else:
      data.update(new_data)
      with open("data.json", mode="w") as data_file:
        json.dump(data, data_file, indent=4)
    finally:
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

website_input = Entry(width=21)
website_input.grid(column=1, row=1, sticky='w')
website_input.focus()

email_input = Entry(width=35)
email_input.grid(column=1, row=2, columnspan=2, sticky='w')
email_input.insert(0, "email@gmail.com")

password_input = Entry(width=21)
password_input.grid(column=1, row=3, sticky='w')

search_button = Button(text="Search", command=search, width=15)
search_button.grid(column=2, row=1, sticky='w')

generate_button = Button(text="Generate Password", command=generate_password, width=15)
generate_button.grid(column=2, row=3, sticky='w')

add_button = Button(text="Add", width=36, command=save_password)
add_button.grid(column=1, row=4, columnspan=2, sticky='w')

window.mainloop()