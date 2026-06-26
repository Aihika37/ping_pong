from turtle import Turtle
import random

class Ball:
    def __init__(self):
        #intial objects
        self.ball = Turtle()
        self.ball.shape("circle")
        self.ball.color("white")
        self.ball.penup()
        self.ball.speed(0)
        self.reset()

    def move(self):
        #moving ball
        self.ball.goto(self.ball.xcor() + self.dx,self.ball.ycor() + self.dy)

    def bounce_y(self):
        #after bouncing moving to the opposite side of screen in y direction
        self.dy *= -1

    def bounce_x(self):
        # after moving out of the screen , coming back
        self.dx *= -1
        self.dx *= 1.05
        self.dy *= 1.05

    def reset(self):
        self.ball.goto(0, 0)
        self.dx = random.choice([-4, 4])
        self.dy = random.choice([-3, 3])

    def ycor(self):
        return self.ball.ycor()

    def xcor(self):
        return self.ball.xcor()

    # collision with paddles
    def check_collision(self, player_paddle, ai_paddle):
        # Top and bottom wall
        if self.ball.ycor() > 240 or self.ball.ycor() < -240:
            self.bounce_y()
        # Right paddle
        if (self.ball.xcor() > 340 and self.ball.distance(ai_paddle) < 50 and self.dx > 0):
            self.bounce_x()
        # Left paddle
        if (self.ball.xcor() < -340 and self.ball.distance(player_paddle) < 50 and self.dx < 0):
            self.bounce_x()

    # scoring
    def check_score(self, width=900):
        #if ball moves right player's point increases
        if self.ball.xcor() > width // 2:
            return "PLAYER"
        # if ball moves left AI's point increases
        if self.ball.xcor() < -width // 2:
            return "AI"
        return None





