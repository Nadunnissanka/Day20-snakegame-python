import turtle as t
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = t.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snack Game V1")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detecting Collation
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()



screen.exitonclick()
