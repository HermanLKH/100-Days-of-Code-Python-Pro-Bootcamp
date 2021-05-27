# TODO 1. get the correct format of tuples of color list extracted from the image using the colorgram module
# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb_colors.append((r, g, b))
#
# print(rgb_colors)
# TODO 2. draw the hirst painting


import turtle as t
import random


turtle = t.Turtle()
t.colormode(255)
turtle.hideturtle()
turtle.penup()
turtle.speed(0)
turtle.setheading(225)
turtle.forward(400)
turtle.setheading(0)
num_of_dots = 100

color_list = [
    (245, 243, 238), (246, 242, 244), (202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50),
    (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73),
    (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158),
    (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129),
    (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)
]

for i in range(1, num_of_dots + 1):
    turtle.dot(20, random.choice(color_list))
    turtle.forward(70)

    if i % 10 == 0:
        turtle.setheading(90)
        turtle.forward(70)
        turtle.setheading(180)
        turtle.forward(700)
        turtle.setheading(0)

# way 2
# can manipulate width and height
# def draw_painting(row, col):
#     current_row = 1
#
#     while current_row <= row:
#         current_col = 1
#         while current_col <= col:
#             turtle.dot(20, random.choice(color_list))
#             current_col += 1
#
#             if current_col <= col:
#                 turtle.forward(70)
#             else:
#                 current_row += 1
#
#         if current_row <= row:
#             turtle.left(90)
#             turtle.forward(70)
#             turtle.left(90)
#             turtle.forward(70 * (col - 1))
#             turtle.right(180)


screen = t.Screen()
screen.exitonclick()
