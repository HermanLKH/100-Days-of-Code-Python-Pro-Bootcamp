import turtle as t


def move_forwards():
    turtle.forward(10)


def move_backwards():
    turtle.backward(10)


def turn_left():
    turtle.left(10)


def turn_right():
    turtle.right(10)


def clear():
    turtle.penup()
    turtle.home()
    turtle.clear()
    turtle.pendown()


turtle = t.Turtle()
screen = t.Screen()
screen.listen()
screen.onkeypress(key="w", fun=move_forwards)
screen.onkeypress(key="s", fun=move_backwards)
screen.onkeypress(key="a", fun=turn_left)
screen.onkeypress(key="d", fun=turn_right)
screen.onkeypress(key="c", fun=clear)
screen.exitonclick()
