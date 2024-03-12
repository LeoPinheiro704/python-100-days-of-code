from turtle import Screen
from snack import Snack
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snack Game")
screen.tracer(0)


snack = Snack()


screen.listen()
screen.onkey(snack.up, "Up")
screen.onkey(snack.down, "Down")
screen.onkey(snack.left, "Left")
screen.onkey(snack.right, "Right")


game_is_on = True
while game_is_on:
  screen.update()
  time.sleep(.1)
  snack.move()
  

screen.exitonclick()
