import turtle
from ball import Ball
from paddle import Paddle
from ai import AI
from scoreboard import Scoreboard
import menu

#Screen setup
wn = turtle.Screen()
wn.title("Ping Pong AI")
wn.bgcolor("black")
wn.setup(width=900, height=500)
wn.tracer(0)

#Game state
state = "MENU"

#Intial Objects
ball = None
player = None
ai = None
ai_paddle = None
scoreboard = None

def start_game(diff, win):
    global ball, player, ai, ai_paddle, scoreboard, state
    # beginning of the game
    state = "PLAYING"
    ball = Ball()
    scoreboard = Scoreboard(win)
    player = Paddle(-400)
    ai_paddle = Paddle(400)
    ai = AI(ai_paddle, diff)
    #setting moving controls
    wn.listen()
    wn.onkeypress(player.go_up, "Up")
    wn.onkeypress(player.go_down, "Down")

def update():
    global state
    if state == "PLAYING":
        ball.move()
        ai.move(ball, ai_paddle)
        ball.check_collision(player, ai_paddle)
        scorer = ball.check_score()
        #adding points
        if scorer == "PLAYER":
            scoreboard.add_player_point()
            ball.reset()
        elif scorer == "AI":
            scoreboard.add_ai_point()
            ball.reset()
        if scoreboard.check_win():
            state = "GAME_OVER"

    wn.update()
    wn.ontimer(update, 20)


def main():
    global state
    #showing menu
    menu_obj = menu.Menu(wn)
    result = menu_obj.show()
    if result is None:
        return
    difficulty, win_score = result
    start_game(difficulty, win_score)
    update()
    wn.mainloop()


def set_state(new_state):
    global state
    state = new_state

main()
