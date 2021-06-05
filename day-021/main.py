# TODO 1. create the screen
# TODO 2. create and move a paddle
# TODO 3. create another paddle
# TODO 4. create the ball and make it move
# TODO 5. detect collision with wall and bounce
# TODO 6. detect collision with paddle
# TODO 7. detect when paddle misses
# TODO 8. keep score

from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time


game_is_on = True

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")

screen.tracer(0)

l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.update()

screen.listen()
screen.onkey(key="w", fun=l_paddle.go_up)
screen.onkey(key="s", fun=l_paddle.go_down)
screen.onkey(key="Up", fun=r_paddle.go_up)
screen.onkey(key="Down", fun=r_paddle.go_down)

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with wall
    if (ball.xcor() > 320 and ball.distance(r_paddle) < 50) or (ball.xcor() < -320 and ball.distance(l_paddle) < 50):
        ball.bounce_x()

    # Detect collision with paddle
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
        l_paddle.increase_speed()
        r_paddle.increase_speed()

    # Detect R paddle misses
    if ball.xcor() > 380:
        scoreboard.l_point()
        ball.reset_position()
        l_paddle.reset_speed()
        r_paddle.reset_speed()

    # Detect L paddle misses
    if ball.xcor() < -380:
        scoreboard.r_point()
        ball.reset_position()
        l_paddle.reset_speed()
        r_paddle.reset_speed()

screen.exitonclick()
