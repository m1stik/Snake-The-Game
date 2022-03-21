from turtle import Turtle
import random

class Food(Turtle):

    # Initial parameters of the object
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.pu()
        #self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("green")
        self.speed("fastest")
        self.refresh()

    # Spawning the food object
    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)