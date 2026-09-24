from turtle import  Screen
import time

from scoreboard import Scoreboard
from snake import Snake
from food import Food
screen = Screen()
screen.setup(width=600, height=600)
screen.title('Snake')
screen.bgpic("background.png")
screen.tracer(0)


snake = Snake()
food = Food()
scoreboard = Scoreboard()
screen.listen()

screen.onkey(fun=snake.up, key='Up')
screen.onkey(fun=snake.down, key='Down')
screen.onkey(fun=snake.left, key='Left')
screen.onkey(fun=snake.right, key='Right')

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    # eat food
    if snake.head.distance(food) < 30:
        food.refresh()
        snake.extend()
        scoreboard.update()

    # Detect walls
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        scoreboard.reset()
        snake.reset()

    #detect body
    for segment in snake.snake_parts[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()


screen.exitonclick()