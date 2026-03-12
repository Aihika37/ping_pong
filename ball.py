from turtle import Turtle
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("black")
        self.penup()
        self.x_move=10
        self.y_move=10
        self.move_speed=0.1
    def move(self):
        self.goto(self.xcor()+self.x_move,self.ycor()+self.y_move)
    def detect_collisions(self):
        if (self.ycor()>280 or self.ycor()<-280):
            self.y_move*=-1





