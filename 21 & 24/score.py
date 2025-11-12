
from turtle import Turtle

ALIGN= "center"
FONT= ("Courier", 20, "normal")

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("new_score.txt", "r") as file:
            self.highscore = int(file.read())
        self.penup()
        self.hideturtle()
        self.color('white')
        self.goto(0, 350)
        self.update_score()


    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.highscore}", align=ALIGN, font=FONT)

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("new_score.txt", "w") as file:
                file.write(f"{self.highscore}")
        self.score = 0
        self.update_score()


    def add(self):
        self.score += 1
        self.update_score()


