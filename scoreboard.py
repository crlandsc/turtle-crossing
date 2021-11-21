from turtle import Turtle

ALIGNMENT = "left"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self, coordinates):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.color("black")
        self.setposition(coordinates)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Level: {self.level}", align=ALIGNMENT, font=FONT)

    def increase_level(self):
        self.clear()
        self.level += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)
