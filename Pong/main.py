from turtle import Screen, Turtle
import time
import stick, ball, score
import random


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Welcome to Pong")
screen.tracer(0)
screen.listen()

right_stick=stick.Stick((380,0))
left_stick=stick.Stick((-390,0))
ball=ball.Ball()
score=score.Score()

screen.onkey(right_stick.move_up, "Up")
screen.onkey(right_stick.move_down, "Down")
screen.onkey(left_stick.move_up, "w")
screen.onkey(left_stick.move_down, "s")


game_is_on = True
while game_is_on:
    ball.move()
    screen.update()
    time.sleep(ball.move_speed)

    if (ball.distance(right_stick) < 50 and ball.xcor()>360) or (ball.distance(left_stick) < 50 and ball.xcor()<-360):
        ball.xmove *=-1
        ball.move_speed *= 0.75

    if ball.xcor() > 370 or ball.xcor() < -370:
        if ball.xcor() > 370:
            score.score_left+=1
        else:
            score.score_right+=1
        ball.goto((0, 0))
        ball.move_speed = 0.05
        ball.setheading(random.randrange(0, 360))


    score.update_scoreboard()
    if score.score_left >= 10 or score.score_right >= 10:
        game_is_on = False

writer = Turtle()
writer.hideturtle()
writer.color("white")
writer.write("Game Over!", align="center",  font=("Arial", 24, "bold"))
print(f"Final Score are: \nPlayer 1: {score.score_left}\nPlayer 2: {score.score_right}" )















screen.exitonclick()