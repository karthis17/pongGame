import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from score import ScoreBord

screen = Screen()
screen.bgcolor("black")
screen.setup(800, 600)
screen.tracer(0)
right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))
ball = Ball()
score = ScoreBord()
highest_point = screen.textinput("set a point to finsh game", "Enter the maximum point need to announce winner")

screen.listen()
screen.onkeypress(fun=right_paddle.move_up, key="Up")
screen.onkeypress(fun=right_paddle.move_down, key="Down")
screen.onkeypress(fun=left_paddle.move_up, key="w")
screen.onkeypress(fun=left_paddle.move_down, key="s")


is_game_on = True
while is_game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move_ball()

    if ball.ycor() >= 300 or ball.ycor() <= -300:
        ball.y_bounce()

    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.x_bounce()

    if ball.xcor() > 390:
        ball.restart_ball()
        score.increase_score_l()

    if ball.xcor() < -390:
        ball.restart_ball()
        score.increase_score_r()

    if score.l_score == int(highest_point) or score.r_score == int(highest_point):
        is_game_on = False
        score.winner()


screen.exitonclick()
