from tkinter import *
import pandas
import random


BACKGROUND_COLOR = "#B1DDC6"

current_card = {}

try:
  data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
  data = pandas.read_csv("data/english_words.csv")
finally:
  to_learn = data.to_dict(orient="records")

def next_card():
  global current_card, flip_timer
  window.after_cancel(flip_timer)
  current_card = random.choice(to_learn)
  canvas.itemconfig(card_title, text="English", fill="black")
  canvas.itemconfig(card_word, text=current_card["english"], fill="black")
  canvas.itemconfig(card_background, image=card_front_img)
  flip_timer = window.after(3000, func=flip_card)

def flip_card():
  canvas.itemconfig(card_title, text="Português", fill="white")
  canvas.itemconfig(card_word, text=current_card["portugues"], fill="white")
  canvas.itemconfig(card_background, image=card_back_img)

def is_know():
  to_learn.remove(current_card)
  data = pandas.DataFrame(to_learn)
  data.to_csv("data/words_to_learn.csv", index=False)
  next_card()

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="Word", font=("Ariel", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)


wrong_button_img = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_button_img, highlightthickness=0, command=next_card)
wrong_button.grid(row=1, column=0)

right_button_img = PhotoImage(file="images/right.png")
right_button = Button(image=right_button_img, highlightthickness=0, command=is_know)
right_button.grid(row=1, column=1)

next_card()

window.mainloop()