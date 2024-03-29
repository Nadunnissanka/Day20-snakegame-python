from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")
FONT_GAME_OVER = ("Arial", 18, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.score = 0
        self.goto(0, 270)
        self.write(f"Score : {self.score}", align=ALIGNMENT, font=FONT)
        self.hideturtle()

    def increase_score(self):
        self.clear()
        self.score += 1
        self.write(f"Score : {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.color("white")
        self.write(f"Game Over!", align=ALIGNMENT, font=FONT_GAME_OVER)
