from turtle import Turtle


STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.segments = []
        self.spawn()
        self.head = self.segments[0]

    def spawn(self):
        # spawn the snake
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle(shape="square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        position = self.segments[-1].pos()
        self.add_segment(position)

    def move(self):
        # movement of snake body
        for i in range(len(self.segments) - 1, 0, -1):
            current_segment = self.segments[i]
            next_segment = self.segments[i - 1]
            current_segment.goto(next_segment.pos())
        # movement of snake head
        self.head.forward(MOVE_DISTANCE)

        # 2nd way
        # # movement of snake head
        # snake_head = self.snake_segments[0]
        # snake_head.left(90)
        # snake_head.forward(20)

        # movement of snake body
        # for snake_segment in self.snake_segments:
        #     if not snake_segment == self.snake_segments[0]:
        #         new_position = self.positions[self.snake_segments.index(snake_segment) - 1]
        #         snake_segment.goto(new_position)

        # # update the new positions of snake segments
        # for i in range(len(self.snake_segments)):
        #     self.positions[i] = self.snake_segments[i].pos()

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(0)
