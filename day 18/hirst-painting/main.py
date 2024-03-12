# import colorgram
# img = r"C:\Users\leona\OneDrive\Documentos\Study\Udemy\Angela Yu\Python - 100 days of code\day 18\hirst-painting\image.jpg"
# rgb_colors = []
# colors = colorgram.extract(img, 30)
# for color in colors:
#     rgb_colors.append((color.rgb.r, color.rgb.g, color.rgb.b))

from turtle import Turtle, Screen
from random import choice


turtle = Turtle()
screen = Screen()
color_list = [(202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]
screen.colormode(255)
turtle.penup()
turtle.hideturtle()
turtle.speed("fast")


def set_position():
  turtle.setheading(225)
  turtle.forward(300)
  turtle.setheading(360)


def draw_row():
  for _ in range(10):
      turtle.pencolor(choice(color_list))
      turtle.dot(20)
      turtle.forward(50)


def going_up(steps):
  turtle.home()
  set_position()
  turtle.left(90)
  turtle.forward(steps)
  turtle.right(90)


set_position()
steps_up = 0
for y in range(10):
  steps_up += 50
  draw_row()
  going_up(steps_up)


screen.exitonclick()