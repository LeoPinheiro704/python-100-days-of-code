from turtle import Turtle
START_POSITIONS = [(0 ,0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snack:
  def __init__(self):
    self.segments = []
    self.create_snack()
    self.head = self.segments[0]
    
  
  def create_snack(self):
    for position in START_POSITIONS:
      segment = Turtle(shape="square")
      segment.color("white")
      segment.penup()
      segment.goto(position)
      self.segments.append(segment)


  def move(self):
    for seg_num in range(len(self.segments) - 1, 0, -1):
      new_x = self.segments[seg_num - 1].xcor()
      new_y = self.segments[seg_num - 1].ycor()
      self.segments[seg_num].goto(new_x, new_y)
    self.head.fd(MOVE_DISTANCE)


  def right(self):
    if self.head.heading() != LEFT:
      self.head.setheading(RIGHT)


  def up(self):
    if self.head.heading() != DOWN:
      self.head.setheading(UP)


  def left(self):
    if self.head.heading() != RIGHT:
      self.head.setheading(LEFT)


  def down(self):
    if self.head.heading() != UP:
      self.head.setheading(DOWN)