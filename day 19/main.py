from turtle import Turtle, Screen
from random import randint

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
bet = screen.textinput(title="Make your bet", prompt="Whick turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

turtles = []

index = 0
y = -130
for index in range(0, 6):
  turtles.append(Turtle(shape="turtle"))
  turtles[index].penup()
  turtles[index].color(colors[index])
  turtles[index].goto(x=-240, y=y)
  index += 1
  y +=50

if bet:
  is_race_on = True

while is_race_on:
  for turtle in turtles:
    if turtle.xcor() > 230:
      is_race_on = False
      winning_color = turtle.pencolor()
      if winning_color == bet:
        print(f"You've won! The {winning_color} turtle is the winner!")
      else:
        print(f"You've lost! The {winning_color} turtle is the winner!")
    rand_distance = randint(0 ,10)
    turtle.fd(rand_distance)

screen.exitonclick()