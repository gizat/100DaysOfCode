from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Arial', 20, 'normal')

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.color('white')
        self.hideturtle()
        self.score = 0
        self.goto(0, 270)
        self.update_score()
        
    
    def increase_score(self):
        self.score += 1


    def update_score(self):
        self.clear()
        self.write(f'SCORE: {self.score}', False, align=ALIGNMENT, font=FONT)

    
    def game_over(self):
        self.goto(0, 0)
        self.write(f'GAME OVER', False, align=ALIGNMENT, font=FONT)