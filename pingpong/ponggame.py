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

r_up_pressed = False
r_down_pressed = False
l_up_pressed = False
l_down_pressed = False

def r_up_press():
    global r_up_pressed
    r_up_pressed = True

def r_down_press():
    global r_down_pressed
    r_down_pressed = True

def l_up_press():
    global l_up_pressed
    l_up_pressed = True

def l_down_press():
    global l_down_pressed
    l_down_pressed = True

def r_up_release():
    global r_up_pressed
    r_up_pressed = False

def r_down_release():
    global r_down_pressed
    r_down_pressed = False

def l_up_release():
    global l_up_pressed
    l_up_pressed = False

def l_down_release():
    global l_down_pressed
    l_down_pressed = False

screen.onkeypress(r_up_press, "Up")
screen.onkeypress(r_down_press, "Down")
screen.onkeypress(l_up_press, "w")
screen.onkeypress(l_down_press, "s")

screen.onkeyrelease(r_up_release, "Up")
screen.onkeyrelease(r_down_release, "Down")
screen.onkeyrelease(l_up_release, "w")
screen.onkeyrelease(l_down_release, "s")

screen.listen()

game_on = True
while game_on:
    time.sleep(0.05)
    if r_up_pressed:
        r_paddle.go_up()
    if r_down_pressed:
        r_paddle.go_down()
    if l_up_pressed:
        l_paddle.go_up()
    if l_down_pressed:
        l_paddle.go_down()
    ball_obj.move()

    if ball_obj.ycor() >= 280:
        ball_obj.sety(280)
        ball_obj.bounce_y()
    elif ball_obj.ycor() <= -280:
        ball_obj.sety(-280)
        ball_obj.bounce_y()
    
    if (ball_obj.distance(r_paddle) < 50 and ball_obj.xcor() > 340) or (ball_obj.distance(l_paddle) < 50 and ball_obj.xcor() < -340):
        ball_obj.bounce_x()

    if ball_obj.xcor() > 380:
        ball_obj.reset_position()
        scoreboard.l_point()
    elif ball_obj.xcor() < -380:
        ball_obj.reset_position()
        scoreboard.r_point()

    screen.update()

screen.exitonclick()
