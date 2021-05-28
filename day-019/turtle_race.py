# TODO 1. create 6 different color turtles which spawn respectively at the starting line


from turtle import Turtle, Screen
import random


def turtle_race():
    colors = ["red", "orange", "yellow", "green", "blue", "purple"]
    all_turtles = []
    x = -440
    y = 300
    is_race_on = False
    winning_color = []

    screen = Screen()
    screen.setup(width=1000, height=700)

    user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a colour: ")

    for color in colors:
        new_turtle = Turtle(shape="turtle")
        new_turtle.color(color)
        new_turtle.penup()
        new_turtle.setpos(x=x, y=y)
        all_turtles.append(new_turtle)
        y -= 120

    if user_bet:
        is_race_on = True

    while is_race_on:
        for turtle in all_turtles:
            rand_distance = random.randint(0, 10)
            turtle.forward(rand_distance)
            if turtle.xcor() > 400:
                winning_color.append(turtle.color()[0])

        if winning_color:
            winning_color = ", ".join(winning_color)
            if user_bet.lower() in winning_color:
                is_play_again = screen.textinput(title="You've won!",
                                                 prompt=f"The {winning_color} turtle is the winner!\n"
                                                        "Do you want to play again?(y/n) ")
            else:
                is_play_again = screen.textinput(title="You've lost...",
                                                 prompt=f"The {winning_color} turtle is the winner.\n"
                                                        "Do you want to play again?(y/n) ")
            if is_play_again == "y":
                for old_turtle in screen.turtles():
                    old_turtle.hideturtle()
                turtle_race()
            else:
                is_race_on = False

    screen.bye()


turtle_race()
