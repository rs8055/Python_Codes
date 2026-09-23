from turtle import Turtle
import random

# class Food(Turtle):
#     def __init__(self):
#         super().__init__()
#         self.shape("circle")
#         self.color("red")
#         self.penup()
#         self.refresh()
#
#     def refresh(self):
#         x_cor = random.randrange(-280, 300, 20)
#         y_cor = random.randrange(-280, 300, 20)
#         self.goto((x_cor, y_cor))

class Food():
    def __init__(self):
        self.segments = []
        self.make_food()

    def make_food(self):
        food=Turtle(shape="circle")
        food.color("red")
        food.penup()
        self.segments.append(food)

    def refresh(self):
        x_cor = random.randrange(-270, 290, 20)
        y_cor = random.randrange(-270, 290, 20)
        self.segments[0].goto((x_cor, y_cor))

