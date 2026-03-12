from turtle import Turtle,Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time
ball=Ball()
s=Scoreboard()
screen=Screen()
screen.title("MY PINGPOG GAME")
screen.setup(width=800,height=600)
screen.bgcolor("white")
screen.tracer(0)
r_paddle=Paddle()
r_paddle.goto(350,0)
l_paddle=Paddle()
l_paddle.goto(-350,0)
screen.listen()
screen.onkey(r_paddle.go_up,"Up")
screen.onkey(r_paddle.go_down,"Down")
screen.onkey(l_paddle.go_up,"u")
screen.onkey(l_paddle.go_down,"d")
game_is_on=True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    ball.detect_collisions()
    if ball.distance(r_paddle) < 50 and ball.xcor() > 340:
        ball.x_move *= -1
        ball.move_speed*=0.9
    if ball.distance(l_paddle) < 50 and ball.xcor() < -340:
        ball.x_move *= -1
        ball.move_speed*=0.9
    if ball.xcor()>380:
        ball.goto(0, 0)
        ball.x_move = -10
        ball.y_move = -10
        ball.move_speed=0.1
        s.l_score+=1
        s.update_scoreboard()
    elif ball.xcor()<-380:
        ball.goto(0, 0)
        ball.x_move = 10
        ball.y_move = 10
        ball.move_speed=0.1
        s.r_score+=1
        s.update_scoreboard()


screen.exitonclick()