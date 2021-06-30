from turtle import Turtle

FONT =("Courier", 80, "normal")
WIN_FONT =("Courier", 25, "normal")
RULE_FONT =("Courier", 13, "normal")

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 180)
        self.write(self.l_score, align= "center", font=FONT)
        self.goto(100, 180)
        self.write(self.r_score, align= "center", font=FONT)

    def l_point(self):
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        self.r_score += 1
        self.update_scoreboard()

    def finish(self, player):
        self.goto(0, 0)
        self.write(f"Player {player} has won the game.", align= "center", font=WIN_FONT)

    def front_page(self):
        self.goto(0, -280)
        self.write(f"The first player to get a 3 point lead wins the game.", align= "center", font=RULE_FONT)
        self.goto(0, -250)
        self.color("white")
        self.pensize(5)
        self.setheading(90)

        for i in range(18):
            self.pendown()
            self.forward(10)
            self.penup()
            self.forward(20)

    def name(self):
        self.color("white")
        self.goto(-150, 250)
        self.write("A", align= "center", font=WIN_FONT)
        self.goto(150, 250)
        self.write("B", align= "center", font=WIN_FONT)