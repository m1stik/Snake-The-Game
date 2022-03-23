from turtle import Turtle

class Scoreboard(Turtle):

    # Initial parameters of the object
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as f:
            self.high_score = int(f.read())
        self.color("white")
        self.speed("fastest")
        self.pu()
        self.hideturtle()
        self.goto(0, 270)
        self.display_score()
    
    # Clear the screen and display currecnt score
    def display_score(self):
        self.clear()
        self.write(f"Score: {self.score} | High Score: {self.high_score}", False, align="center", font=("Consolas", 15, "normal"))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as f:
                f.write(str(self.high_score))

        self.score = 0
        self.display_score()

    # Increase points, update display output
    def add_point(self):
        self.score += 1
        self.display_score()