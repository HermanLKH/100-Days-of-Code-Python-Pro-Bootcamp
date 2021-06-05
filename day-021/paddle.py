from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__(shape="square")
        self.penup()
        self.setpos(position)
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.move_speed = 20

    def go_up(self):
        new_y = self.ycor() + self.move_speed
        self.sety(new_y)

    def go_down(self):
        new_y = self.ycor() - self.move_speed
        self.sety(new_y)

    def increase_speed(self):
        self.move_speed *= 1.1

    def reset_speed(self):
        self.move_speed = 10
