from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Arial', 24, 'normal')

class Scoreboard(Turtle):

  def __init__(self):
    super().__init__()
    self.score = 0
    self.hideturtle()
    self.penup()
    self.color("white")
    self.speed("fastest")
    self.goto(x=0, y=260)
    self.show_score()

  def to_score(self):
    self.score += 1
    self.show_score()
    
  def show_score(self):
    self.clear()
    self.write(f"Score = {self.score}", align=ALIGNMENT, font=FONT)

  def game_over(self):
    self.goto(x=0, y=0)
    self.write(f"GAME OVER", align=ALIGNMENT, font=FONT)
