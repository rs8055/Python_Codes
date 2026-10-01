from turtle import Turtle

class Stick(Turtle):
    def __init__(self, position):
        super().__init__()
        self.position = position
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=4)
        self.setheading(90)
        self.goto(self.position)


    def move_up(self):
        if self.ycor() < 250:
            self.forward(10)

    def move_down(self):
        if self.ycor() > -240:
            self.backward(10)