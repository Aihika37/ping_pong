from turtle import Turtle

class Scoreboard:
    def __init__(self, win_score=5):
        #intial objects
        self.player_score = 0
        self.ai_score = 0
        self.win_score = win_score
        self.writer = Turtle()
        self.writer.hideturtle()
        self.writer.penup()
        self.writer.color("white")
        self.update_display()

    def update_display(self):
        #updating scores
        self.writer.clear()
        self.writer.goto(0, 210)
        self.writer.write(
            f"{self.player_score}  :  {self.ai_score}",
            align="center",
            font=("Arial", 28, "bold")
        )
        self.writer.goto(0, 180)
        #initial target to win
        self.writer.write(
            f"First to {self.win_score}",
            align="center",
            font=("Arial", 14, "normal")
        )

    def add_player_point(self):
        self.player_score += 1
        self.update_display()

    def add_ai_point(self):
        self.ai_score += 1
        self.update_display()

    def check_win(self):
        #deciding winners
        if self.player_score >= self.win_score:
            self.winner = "PLAYER"
            return True
        if self.ai_score >= self.win_score:
            self.winner = "AI"
            return True
        return False

    def reset(self):
        self.player_score = 0
        self.ai_score = 0
        self.update_display()
