from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.hideturtle()
        self.penup()
        self.speed("fastest")
        self.level = 1
        self.update_scoreboard()
    
    def update_scoreboard(self):
        self.clear()
        self.goto(-280, 250)
        self.write(f"Level: {self.level}", font=FONT)
    
    def level_up(self):
        self.level += 1
        self.update_scoreboard()
        
    def game_over(self):
        self.goto(x=0, y=0)
        self.write(f"GAME OVER", align="center", font=FONT)