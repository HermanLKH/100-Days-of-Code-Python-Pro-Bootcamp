# TODO 1. draw a square
# for _ in range(4):
#     tim.forward(100)
#     tim.right(90)
# TODO 2. draw dotted-line
# for i in range(15):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()
# TODO 3. draw a triangle, square, pentagon, hexagon, heptagon, octagon, nonagon, decagon
# def draw_shape(num_sides):
#     external_angle = 360 / num_sides
#     for _ in range(num_sides):
#         tim.right(external_angle)
#         tim.forward(100)
#
#
# color_list = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen",
#               "wheat", "SlateGray", "SeaGreen"]
#
# for shape_side in range(3, 11):
#     color = random.choice(color_list)
#     tim.color(color)
#     draw_shape(shape_side)
# TODO 4. draw a random walk
# for _ in range(200):
#     direction = random.choice(directions)
#     color = random_color()
#     tim.setheading(direction)
#     tim.color(color)
#     tim.forward(30)
# TODO 5. generate random rgb color
# t.colormode(255)
# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     return r, g, b
# TODO 6. draw a spirograph


import turtle as t
import random


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b


tim = t.Turtle()
tim.speed(0)
tim.pensize(2)
t.colormode(255)


def draw_spirograph(size_of_gap):
    n = int(360 / size_of_gap)
    for _ in range(n):
        tim.color(random_color())
        tim.right(size_of_gap)
        tim.circle(100)


draw_spirograph(5)
screen = t.Screen()
screen.exitonclick()
