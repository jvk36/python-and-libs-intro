from turtle import Turtle
ALIGN="center"
FONT=("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.goto(0, 260)
        self.color("white")
        self.write_score()

    def write_score(self):
        self.clear()
        self.write(f"Score: {self.score}", align=ALIGN, font=FONT)

    def update_scoreboard(self):
        self.score += 1
        self.write_score()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGN, font=FONT)
