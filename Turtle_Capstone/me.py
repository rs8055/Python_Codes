from turtle import Turtle

class Me(Turtle):
    def __init__(self):
        super().__init__()
        self.color("green")
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.goto(0,-380)


    def move(self):
        if self.ycor() < 360:
            self.forward(10)
