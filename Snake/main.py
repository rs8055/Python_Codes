from turtle import Turtle, Screen
import snake
import food
import time
import scoreboard

screen = Screen()
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.title("Snake Game")
screen.tracer(0)

my_snake = snake.Snake()
food=food.Food()
food.refresh()
sb=scoreboard.Scoreboard()
screen.listen()

screen.onkey(my_snake.move_left, "Left")
screen.onkey(my_snake.move_right, "Right")
screen.onkey(my_snake.move_up, "Up")
screen.onkey(my_snake.move_down, "Down")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    my_snake.move()
    if my_snake.segments[0].distance(food.segments[0]) < 15:
        my_snake.extend()
        sb.score += 1
        food.refresh()
    sb.update_scoreboard()
    if my_snake.strike():
        game_is_on = False


print(f"Game Over. Your score is {sb.score}.")
















screen.exitonclick()
