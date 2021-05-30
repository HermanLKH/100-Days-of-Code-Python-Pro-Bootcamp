from turtle import Turtle


FONT = ("Arial", 12, "bold")
ALIGNMENT = "center"


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.speed("fastest")
        self.goto(x=0, y=270)
        self.color("white")
        self.score = 0
        self.write(f"Score: {self.score}", align=ALIGNMENT, move=False, font=FONT)

    def update_scoreboard(self):
        self.increase_score()
        self.write(f"Score: {self.score}", align=ALIGNMENT, move=False, font=FONT)

    def increase_score(self):
        self.clear()
        self.score += 1

    def game_over(self):
        self.goto(x=0, y=0)
        self.write("Game Over.", align="center", move=False, font=("Arial", 12, "bold"))
