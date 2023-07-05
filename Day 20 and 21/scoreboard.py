from turtle import Turtle

class Score(Turtle):
    def __init__(self):
     super().__init__()
     self.color("White")
     self.penup()
     self.hideturtle()
     self.goto(0, 260)
     self.score=0
     self.write(f"Score: {self.score}", align="center", font=("Courier", 24, "normal"))
    def score_up(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", align="center", font=("Courier", 24, "normal"))
    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align="center", font=("Courier", 24, "normal"))
       
