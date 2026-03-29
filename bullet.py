import turtle

class Bullet(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("yellow")
        self.penup()
        self.shapesize(stretch_wid=0.2, stretch_len=0.8)
        self.hideturtle()
        self.speed(0)
        self.state = "ready"

    def fire(self, player):
        if self.state == "ready":
            self.state = "fire"
            self.goto(player.xcor(), player.ycor() + 10)
            self.showturtle()

    def move(self):
        if self.state == "fire":
            self.sety(self.ycor() + 20)

            if self.ycor() > 300:
                self.hideturtle()
                self.state = "ready"