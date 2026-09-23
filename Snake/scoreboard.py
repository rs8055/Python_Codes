from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.ht()
        self.color("white")
        self.penup()
        self.goto(0,280)

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}", align="center", font=("Arial", 12, "normal"))