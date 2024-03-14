from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

LEFT_POSITION = (-350, 0)
RIGHT_POSITION = (350, 0)

screen = Screen()
screen.setup(height=600, width=800)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

r_paddle = Paddle(RIGHT_POSITION)
l_paddle = Paddle(LEFT_POSITION)
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")

game_is_on = True
while game_is_on:
  screen.update()
  time.sleep(ball.move_speed)
  ball.move()

  # Detect collision with wall
  if ball.ycor() > 280 or ball.ycor() < - 280:
    ball.bounce_y()
  
  # Detect collision with r_paddle
  if (ball.distance(r_paddle) < 50 and ball.xcor() > 320) or (ball.distance(l_paddle) < 50 and ball.xcor() < -320):
    ball.bounce_x()

  # Detect when the right paddle misses
  if ball.xcor() > 380:
    scoreboard.l_to_score()
    ball.reset_position()
    print("point")

  # Detect when the left paddle misses
  if ball.xcor() < -380:
    scoreboard.r_to_score()
    ball.reset_position()


screen.exitonclick()