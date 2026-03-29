import turtle
import random

class Enemy(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("red")
        self.penup()
        x = random.randint(-200, 200)
        y = random.randint(100, 250)
        self.goto(x, y)

    def move(self):
        self.sety(self.ycor() - 2)