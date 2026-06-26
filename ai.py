import random
import time

class AI:
    def __init__(self,paddle, difficulty="Medium"):
        #intial objects
        self.paddle = paddle
        self.set_difficulty(difficulty)
        self.last_move_time = time.time()

    def set_difficulty(self, difficulty):
        self.difficulty = difficulty
        #setting controls according to difficulty
        if difficulty == "Easy":
            self.speed = 3
            self.delay = 0.18
            self.error = 40
        elif difficulty == "Medium":
            self.speed = 5
            self.delay = 0.10
            self.error = 20
        else:
            self.speed = 7
            self.delay = 0.03
            self.error = 5

    def move(self, ball, ai_paddle):
        #skipping time frames according to difficulty
        if time.time() - self.last_move_time < self.delay:
            return
        target_y = ball.ycor()#noting ball's coordinates
        target_y += random.randint(-self.error, self.error)#setting an error
        #moving accordingly after the error
        if ai_paddle.ycor() < target_y:
            ai_paddle.sety(ai_paddle.ycor() + self.speed)
        elif ai_paddle.ycor() > target_y:
            ai_paddle.sety(ai_paddle.ycor() - self.speed)
        self.last_move_time = time.time()