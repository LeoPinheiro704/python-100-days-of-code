from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snack Game")

segments = []
xposition = 0
# xpositions = [(0 ,0), (-20, 0), (-40, 0)]
for index in range(3):
  segments.append(Turtle(shape="square"))
  segments[index].color("white")
  segments[index].goto(x=xposition, y=0)
  xposition -= 20


screen.exitonclick()