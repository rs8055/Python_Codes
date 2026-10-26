from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "violet", "purple"]

class Cars():
    def __init__(self):
        self.segments = []
        self.update_segments()
        self.speed = 5

    def update_segments(self):
        random_check = random.randint(0,6)
        if random_check == 0:
            new_car = Turtle()
            new_car.shape("square")
            new_car.color(random.choice(COLORS))
            new_car.turtlesize(stretch_wid=1,stretch_len=2)
            new_car.setheading(180)
            new_car.penup()
            new_car.goto(380,random.randrange(-330,350, 20))
            self.segments.append(new_car)

    def move(self):
        for segment in self.segments:
            segment.forward(self.speed)
        self.update_segments()