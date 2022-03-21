from turtle import Turtle

# Constant variables
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    # Initial parameters of the object
    def __init__(self):
        self.snake_parts = []
        for _ in range(3): self.add_snake()

    # Adding a part of the snake, putting it in the array
    def add_snake(self):
        snake_part = Turtle()
        snake_part.shape("square")
        snake_part.color("white")
        snake_part.speed("fastest")
        snake_part.pu()
        self.snake_parts.append(snake_part)

    # Moving a head of the snake and each its segment
    def move(self):
        for part_num in range(len(self.snake_parts) - 1, 0, -1):
            new_x = self.snake_parts[part_num - 1].xcor()
            new_y = self.snake_parts[part_num - 1].ycor()
            self.snake_parts[part_num].goto(new_x, new_y)
        
        self.snake_parts[0].forward(MOVE_DISTANCE)

    # Handling controls
    def up(self):
        if self.snake_parts[0].heading() != DOWN:
            self.snake_parts[0].setheading(UP)
    def down(self):
        if self.snake_parts[0].heading() != UP:
            self.snake_parts[0].setheading(DOWN)
    def left(self):
        if self.snake_parts[0].heading() != RIGHT:
            self.snake_parts[0].setheading(LEFT)
    def right(self):
        if self.snake_parts[0].heading() != LEFT:
            self.snake_parts[0].setheading(RIGHT)