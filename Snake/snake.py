from turtle import Turtle

INITIAL_POSITIONS = [(0,0), (-20,0), (-40,0)]
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

class Snake:
    def __init__(self):
        self.segments = []
        self.make_snake()

    def make_snake(self):
        for position in INITIAL_POSITIONS:
            new_turtle = Turtle(shape="square")
            new_turtle.color("white")
            new_turtle.penup()
            new_turtle.goto(position)
            self.segments.append(new_turtle)

    def move(self):
        for position_number in range(len(self.segments) - 1, 0, -1):
            x_cor = self.segments[position_number - 1].xcor()
            y_cor = self.segments[position_number - 1].ycor()
            self.segments[position_number].goto(x_cor, y_cor)
        self.segments[0].forward(20)

    def extend(self):
        new_turtle = Turtle(shape="square")
        new_turtle.color("white")
        new_turtle.penup()
        x_cor = self.segments[len(self.segments) - 1].xcor()
        y_cor = self.segments[len(self.segments) - 1].ycor()
        new_turtle.goto(x_cor, y_cor)
        self.segments.append(new_turtle)

    def strike(self):
        if self.segments[0].xcor()>285 or self.segments[0].xcor()<-285 or self.segments[0].ycor()>285 or self.segments[0].ycor()<-285:
            return True
        elif any(self.segments[0].position() == segment.position() for segment in self.segments[1:]):
            return True
        else:
            return False


    def move_left(self):
        if self.segments[0].heading() != RIGHT:
            self.segments[0].setheading(180)
            # self.move()

    def move_right(self):
        if self.segments[0].heading() != LEFT:
            self.segments[0].setheading(0)
            # self.move()

    def move_up(self):
        if self.segments[0].heading() != DOWN:
            self.segments[0].setheading(90)
            # self.move()

    def move_down(self):
        if self.segments[0].heading() != UP:
            self.segments[0].setheading(270)
            # self.move()

