from turtle import Screen
from paddle import Paddle
from Ball import ball
import time
from scoreboard import board
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball_obj = ball()

scoreboard = board()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_on = True
while game_on:
    time.sleep(0.05)
    ball_obj.move()

    if ball_obj.ycor() >= 280:
        ball_obj.sety(280)
        ball_obj.bounce_y()
    elif ball_obj.ycor() <= -280:
        ball_obj.sety(-280)
        ball_obj.bounce_y()
    
    if (ball_obj.distance(r_paddle) < 50 and ball_obj.xcor() > 340) or (ball_obj.distance(l_paddle) < 50 and ball_obj.xcor() < -340):
        ball_obj.bounce_x()

    if ball_obj.xcor() > 380 or ball_obj.xcor() < -380:
        break
    screen.update()

screen.exitonclick()
