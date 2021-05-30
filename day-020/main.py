# TODO 1. create a snake body
# TODO 2. move the snake
# TODO 3. control the snake
# TODO 4. detect collision with food
# TODO 5. create a scoreboard
# TODO 6. detect collision with wall
# TODO 7. increase snake segment once food swallowed
# TODO 8. detect collision with snake body
# create 3 class - snake, food, score
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time


game_is_on = True
snake_segments = []
positions = [(0, 0), (-20, 0), (-40, 0)]

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        snake.extend()
        food.refresh()
        scoreboard.update_scoreboard()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 260 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()
