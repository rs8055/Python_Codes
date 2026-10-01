from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score_left = 0
        self.score_right = 0
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0,-300)
        self.setheading(90)
        for i in range(56):
            if i%2==0:
                self.penup()
                self.forward(10)
                self.pendown()
            else:
                self.forward(10)
        self.write(f"Score:",
            align="center",
            font=("Arial", 12, "normal"))
        self.penup()
        self.goto(-360,260)
        self.write(f"Player 1",
                   align="center",
                   font=("Arial", 12, "normal"))
        self.goto(360, 260)
        self.write(f"Player 2",
                   align="center",
                   font=("Arial", 12, "normal"))
        self.score_right_tur = self.score_turtle((40, 240))
        self.score_left_tur = self.score_turtle((-40, 240))

    def score_turtle(self,position):
        self.score_tur = Turtle()
        self.score_tur.hideturtle()
        self.score_tur.color("white")
        self.score_tur.penup()
        self.score_tur.goto(position)
        return self.score_tur

    def update_scoreboard(self):
        self.score_right_tur.clear()
        self.score_right_tur.write(f"{self.score_right}", align="center", font=("Arial", 12, "normal"))

        self.score_left_tur.clear()
        self.score_left_tur.write(f"{self.score_left}", align="center", font=("Arial", 12, "normal"))
