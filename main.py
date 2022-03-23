from turtle import Screen
from snake import Snake
from food import Food
from score import Scoreboard
import time

game_is_on = True

# Setup the display
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake The Game")
screen.tracer(0)

# Initializing objects
snake = Snake()
food = Food()
scoreboard = Scoreboard()

# Handling a control of the snake
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# Main game loop
while game_is_on:

    # Update screen content, delay, move the snake
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect a collision with the food
    if snake.snake_parts[0].distance(food) < 21:
        food.refresh()
        snake.add_snake()
        scoreboard.add_point()

    # Detect a collision with the wall
    if snake.snake_parts[0].xcor() > 290 or snake.snake_parts[0].xcor() < -290 or snake.snake_parts[0].ycor() > 290 or snake.snake_parts[0].ycor() < -290:
        scoreboard.reset()
        snake.reset()

    # Detect a collision with the tail
    for part in snake.snake_parts[1:]:
        if snake.snake_parts[0].distance(part) < 10:
            scoreboard.reset()
            snake.reset()

screen.exitonclick()