from turtle import Screen
from src.pong_paddle import Paddle
from src.pong_ball import Ball
from src.pong_scoreboard import Scoreboard
import time


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("pong")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(r_paddle.up, "Up")
screen.onkeypress(r_paddle.down, "Down")
screen.onkeypress(l_paddle.up, "w")
screen.onkeypress(l_paddle.down, "s")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()
    # handle collision with the top and bottom walls
    if ball.ycor() >= 280 or ball.ycor() <= -280:
        ball.bounce_y()
    # handle collision with the left and write paddles
    if ball.distance(r_paddle) <= 50 and ball.xcor() >= 320 or ball.distance(l_paddle) <= 50 and ball.xcor() <= -320:
        ball.bounce_x()
        ball.increase_speed()
    # handle ball going out of bounds to the right
    if ball.xcor() >= 380:
        ball.reset_position()
        scoreboard.l_point()
    # handle ball going out of bounds to the left
    if ball.xcor() <= -380:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()
