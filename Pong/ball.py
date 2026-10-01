from turtle import Turtle
import random
import math

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("white")
        self.setheading(random.randrange(0,360))
        self.xmove = 10
        self.ymove = 10

    def move(self):
        if self.ycor()>280 or self.ycor()<-275:
            self.ymove *=-1

        x_cor = self.xcor()
        y_cor = self.ycor()
        if self.heading()>= 0 and self.heading()<90:
            self.goto(x_cor + self.xmove, y_cor + self.ymove)
        elif self.heading()>=90 and self.heading()<180:
            self.goto(x_cor - self.xmove, y_cor + self.ymove)
        elif self.heading()>=180 and self.heading()<270:
            self.goto(x_cor - self.xmove, y_cor - self.ymove)
        else:
            self.goto(x_cor + self.xmove, y_cor - self.ymove)
