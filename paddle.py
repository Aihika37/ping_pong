from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, x):
        super().__init__()
        #intializing the paddle at x
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(x, 0)

    #moving up
    def go_up(self):
        if self.ycor() < 200:
            self.sety(self.ycor() + 20)

    #moving down
    def go_down(self):
        if self.ycor() > -200:
            self.sety(self.ycor() - 20)
