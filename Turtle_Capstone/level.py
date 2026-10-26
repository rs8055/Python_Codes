from turtle import Turtle

class Level(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.hideturtle()
        self.penup()
        self.score = 0
        self.goto(0,373)
        self.write(f"Level {self.score}", align="center", font=("Arial", 18, "normal"))

    def update_scoreboard(self):
        self.clear()
        self.score += 1
        self.write(f"Level {self.score}", align="center", font=("Arial", 18, "normal"))

    def game_over(self):
        self.goto(0,0)
        self.write("Game Over", align="center", font=("Arial", 22, "normal"))

