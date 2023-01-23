from turtle import Turtle


class ScoreBord(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.l_score = 0
        self.r_score = 0
        self.score_position()

    def score_position(self):
        self.goto(-150, 200)
        self.write(f"{self.l_score}", align="center", font=("Poppins", 70, "normal"))
        self.goto(150, 200)
        self.write(f"{self.r_score}", align="center", font=("Poppins", 70, "normal"))

    def increase_score_l(self):
        self.clear()
        self.l_score += 1
        self.score_position()

    def increase_score_r(self):
        self.clear()
        self.r_score += 1
        self.score_position()

    def winner(self):
        if self.r_score > self.l_score:
            self.goto(0, 0)
            self.color("white")
            self.write(f"""Game OverThe 
            winner is Right side Player {self.r_score}""", align="center", font=("Poppins", 23, "normal"))

        if self.l_score > self.r_score:
            self.goto(0, 0)
            self.color("white")
            self.write(f"""
                    Game Over 
            The Winner is left side player 
                    Score : {self.l_score}""", align="center", font=("Poppins", 23, "normal"))
