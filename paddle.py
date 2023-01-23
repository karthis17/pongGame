from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.color("white")
        self.goto(position)

    # Add movement for paddle.
    def move_up(self):
        """ Move the paddle upward for an 20 pix"""
        if self.ycor() != 240:
            new_y = self.ycor() + 20
            self.goto(self.xcor(), new_y)

    def move_down(self):
        """ Move the paddle downward for an 20 pix"""
        if self.ycor() != -240:
            new_y = self.ycor() - 20
            self.goto(self.xcor(), y=new_y)
