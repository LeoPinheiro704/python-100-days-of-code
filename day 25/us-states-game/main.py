import turtle
import pandas

FONT = ('Arial', 8, 'normal')

screen = turtle.Screen()
screen.title("U.S. States Game")
screen.setup(width=725, height=491)
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


data = pandas.read_csv("50_states.csv")
total_states = len(data)
states_list = data["state"].to_list()
guessed_states = []

while len(guessed_states) < 50:
  answer_state =  screen.textinput(title=f"{len(guessed_states)}/{total_states} States Correct", prompt="What's another state's name?").title()
  if answer_state == 'Exit':
    missing_states = [state for state in states_list if state not in guessed_states]
    new_data = pandas.DataFrame(missing_states)
    new_data.to_csv("states_to_learn.csv")
    break
  elif answer_state in states_list:
    guessed_states.append(answer_state)
    t = turtle.Turtle()
    t.hideturtle()
    t.penup()
    state_data = data[data.state == answer_state]
    t.goto(x=int(state_data.x.item()), y=int(state_data.y.item()))
    t.write(f"{answer_state}", align="center", font=FONT)

