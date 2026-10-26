from turtle import Turtle, Screen
from me import Me
from level import Level
from cars import Cars
import time

my_screen = Screen()
my_screen.setup(width=800, height=800)
my_screen.title("Turtle Capstone")
my_screen.tracer(0)
my_screen.listen()

my_turtle = Me()
my_level = Level()
car = Cars()

my_screen.onkey(my_turtle.move, "Up")

game_is_on = True
while game_is_on:
    my_screen.update()
    time.sleep(0.1)
    car.move()

    if my_turtle.distance(my_level)<20:
        my_level.update_scoreboard()
        my_turtle.goto(0,-380)
        car.speed+=2

    if any(my_turtle.distance(cars)<25 for cars in car.segments):
        my_level.game_over()
        game_is_on = False


my_screen.exitonclick()
