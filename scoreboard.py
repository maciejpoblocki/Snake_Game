from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(0,260)
        self.score = 0
        self.write(f"Score: {self.score}", align="center", font=('Courier', 15, 'normal'))
        self.hideturtle()

    def update(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", align="center", font=('Courier', 15,"normal"))

    def game_over(self):
        self.goto(0,0)
        self.write("Game over. ", align="center", font= ("Courier",15,"normal"))
