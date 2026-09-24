from turtle import Turtle

POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self):
        self.snake_parts = []
        self.positions = POSITIONS
        self.create_body()
        self.head = self.snake_parts[0]

    def create_body(self):
        for position in POSITIONS:
            self.add_segment(position)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def down(self):
        if self.head.heading() != UP:

            self.head.setheading(DOWN)

    def move(self):
        for seg_num in range(len(self.snake_parts) - 1, 0, -1):
            new_x = self.snake_parts[seg_num - 1].xcor()
            new_y = self.snake_parts[seg_num - 1].ycor()
            self.snake_parts[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def add_segment(self,position):
        snake = Turtle(shape='square')
        snake.color('red')
        snake.penup()
        snake.goto(position)
        self.snake_parts.append(snake)

    def extend(self):
        self.add_segment(self.snake_parts[-1].position())

    def reset(self):
        for seg in self.snake_parts:
            seg.goto(1000,1000)
        self.snake_parts.clear()
        self.create_body()
        self.head = self.snake_parts[0]