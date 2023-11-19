FONT = ("Courier", 18, "normal")
import turtle

class Scoreboard(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.goto(-270,250)
        self.hideturtle()
        self.level = 1
        self.update_scoreboard()


    def update_scoreboard(self):
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def game_over(self):
        self.penup()
        self.goto(0,0)
        self.write("GAME OVER", align="center", font=FONT)

    def increase_level(self):
        self.level += 1
        self.clear()
        self.update_scoreboard()
