from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(0,260)
        self.score = 0
        with open("High_Score.txt",'r') as file:
            self.high_score = int(file.read())
            file.close()
        self.write(f"Score: {self.score} High score: {self.high_score}", align="center", font=('Courier', 15, 'normal'))
        self.hideturtle()

    def update(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score} High score: {self.high_score}", align="center", font=('Courier', 15, 'normal'))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("High_Score.txt", 'w') as file:
                file.write(str(self.high_score))
                file.close()
        self.score = -1
        self.update()