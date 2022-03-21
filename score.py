from turtle import Turtle

class Scoreboard(Turtle):

    # Initial parameters of the object
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.speed("fastest")
        self.pu()
        self.hideturtle()
        self.goto(0, 270)
        self.display_score()
    
    # Clear the screen and display currecnt score
    def display_score(self):
        self.clear()
        self.write(f"Score: {self.score}", False, align="center", font=("Consolas", 15, "normal"))

    # Clear the screen, display the game over message
    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write(f"Game over! You score is: {self.score}", False, align="center", font=("Consolas", 20, "normal"))

    # Increase points, update display output
    def add_point(self):
        self.score += 1
        self.display_score()