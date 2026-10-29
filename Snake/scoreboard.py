from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt","r") as file:
            self.high_score = int(file.read())
        # self.high_score = 0
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
            with open("data.txt", "w") as file_1:
                file_1.write(f"{self.high_score}")
        self.score = 0