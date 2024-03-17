from turtle import Screen
from snack import Snack
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snack Game")
screen.tracer(0)

snack = Snack()
food = Food()
scoreboard = Scoreboard()

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

    # detect collision with food
    if snack.head.distance(food) < 15:
        food.refresh()
        snack.extend()
        scoreboard.to_score()

    # Detect collision with wall
    if snack.head.xcor() > 280 or snack.head.xcor() < -280 or snack.head.ycor() > 280 or snack.head.ycor() < -280:
        scoreboard.reset()
        snack.reset()

    # Detect collision with tail
    for segment in snack.segments[1:]:
        if snack.head.distance(segment) < 10:
            scoreboard.reset()
            snack.reset()

screen.exitonclick()
