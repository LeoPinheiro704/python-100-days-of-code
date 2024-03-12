from turtle import Turtle, Screen
from random import choice, random


timmy = Turtle()

def random_color():
  rand_color = (random(), random(), random())
  timmy.color(rand_color)


def square():
  for _ in range(4):
    timmy.forward(100)
    timmy.right(90)


def draw_shape(side):
  random_color()
  degree = 360 / side
  for _ in range(side):
    timmy.forward(100)
    timmy.right(degree)


def dashed_line():
  for _ in range(25):
    timmy.forward(10)
    timmy.penup()
    timmy.forward(10)
    timmy.pendown()


def random_walk():
  timmy.width(10)
  timmy.speed(10)
  directions = [0, 90, 180, 270]
  for _ in range(100):
    random_color()
    timmy.setheading(choice(directions))
    timmy.fd(20)


def spirograph(gap):
  timmy.speed("fastest")
  for _ in range(int(360 / gap)):
    random_color()
    timmy.setheading(timmy.heading() + gap)
    timmy.circle(120, 360)

spirograph(2)

screen = Screen()
screen.exitonclick()