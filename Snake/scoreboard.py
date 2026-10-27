from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.ht()
        self.color("white")
        self.penup()
        self.goto(0,280)

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align="center", font=("Arial", 12, "normal"))

    def reset_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0