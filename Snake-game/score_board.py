from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 16, "normal")

class Score_Board(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 220)
        self.update_score()
    
    def update_score(self):
        self.write(arg= f"Score: {self.score}", align= ALIGNMENT, font= FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()

    def game_over(self):
        self.goto(0, 0)
        self.write(arg="Game Over!", align= ALIGNMENT, font=FONT)