from turtle import Turtle
from gameconstants import SCOREBOARD_POSITION, SCOREBOARD_ALIGNMENT, SCOREBOARD_FONT

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, SCOREBOARD_POSITION)
        self.print_score()

    def increment_score(self):
        self.score += 1
        self.clear()
        self.print_score()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=SCOREBOARD_ALIGNMENT, font=SCOREBOARD_FONT)

    def print_score(self):
        self.write(f"Score: {self.score}", align=SCOREBOARD_ALIGNMENT, font=SCOREBOARD_FONT)
