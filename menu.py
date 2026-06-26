from turtle import Turtle, Screen

class Menu:
    def __init__(self,screen):
        #intialising the objects
        self.screen = Screen()
        self.writer = Turtle()
        self.writer.hideturtle()
        self.writer.penup()
        self.writer.color("white")
        self.difficulties = ["Easy", "Medium", "Hard"]
        self.index = 1
        self.win_scores = [5, 7, 10]
        self.win_index = 0
        self.start = False
        self.quit = False

    def draw(self):
        #setting the menu screen
        self.writer.clear()
        self.writer.goto(0, 180)
        self.writer.write("🏓 PING PONG",align="center",font=("Arial", 30, "bold"))
        self.writer.goto(0, 80)
        self.writer.write("Press ENTER to Start",align="center",font=("Arial", 18, "normal"))
        self.writer.goto(0, 30)
        self.writer.write(f"Difficulty : {self.difficulties[self.index]}",
            align="center",font=("Arial", 20, "bold"))
        #displaying the instructions
        self.writer.goto(0, -20)
        self.writer.write(
            "W / S to change Win Score",
            align="center",
            font=("Arial", 14, "normal")
        )
        self.writer.goto(0, -60)
        self.writer.write(f"Win Score : {self.win_scores[self.win_index]}",
            align="center",font=("Arial", 20, "bold"))
        self.writer.goto(0, -110)
        self.writer.write("A / D to change difficulty",
            align="center",font=("Arial", 14, "normal"))
        self.writer.goto(0, -80)
        self.writer.write("Press Q to Quit",
            align="center",font=("Arial", 16, "normal"))
    
    #increasing the win score
    def harder_win(self):
        if self.win_index < len(self.win_scores) - 1:
            self.win_index += 1
        self.draw()
        
    #decreasing the win score
    def easier_win(self):
        if self.win_index > 0:
            self.win_index -= 1
        self.draw()
    
    #increasing difficulty
    def harder_difficulty(self):
        if self.index < len(self.difficulties) - 1:
            self.index += 1
        self.draw()
    
    #decreasing difficulty
    def easier_difficulty(self):
        if self.index > 0:
            self.index -= 1
        self.draw()

    def start_game(self):
        self.start = True

    def quit_game(self):
        self.quit = True

    def show(self):
        self.draw()
        #setting up keys based on instructions
        self.screen.listen()
        self.screen.onkey(self.easier_difficulty, "a")
        self.screen.onkey(self.harder_difficulty, "d")
        self.screen.onkey(self.easier_win, "s")
        self.screen.onkey(self.harder_win, "w")
        self.screen.onkey(self.start_game, "Return")
        self.screen.onkey(self.quit_game, "q")
        while not self.start and not self.quit:
            self.screen.update()
        self.writer.clear()
        if self.quit:
            self.screen.bye()
            return None
        return self.difficulties[self.index], self.win_scores[self.win_index]
