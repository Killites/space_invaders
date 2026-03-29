import turtle

class Player(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.shape("triangle")
        self.color("white")
        self.penup()
        self.setheading(90)
        self.goto(0, -250)

    def move_left(self):
        x = self.xcor()
        if x > -280:
            self.setx(x - 20)

    def move_right(self):
        x = self.xcor()
        if x < 280:
            self.setx(x + 20)