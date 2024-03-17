from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Arial', 24, 'normal')


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.high_score = 0
        self.score = 0
        self.get_high_score()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.speed("fastest")
        self.goto(x=0, y=260)
        self.show_score()

    def get_high_score(self):
        with open("data.txt") as file:
            self.high_score = int(file.read())

    def to_score(self):
        self.score += 1
        self.show_score()

    def show_score(self):
        self.clear()
        self.write(f"Score = {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            with open("data.txt", mode="w") as file:
                file.write(f"{self.score}")
        self.get_high_score()
        self.score = 0
        self.show_score()

    # def game_over(self):
    #   self.goto(x=0, y=0)
    #   self.write(f"GAME OVER", align=ALIGNMENT, font=FONT)
