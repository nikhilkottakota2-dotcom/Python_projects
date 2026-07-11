#this is also related to the pong game 
from turtle import Turtle

class ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()

    def move(self):
        new_x = self.xcor() + 10
        new_y = self.ycor() + 10
        self.goto(new_x, new_y)

    def move(self):
        new_x = self.xcor()+10
        new_y = self.ycor()+10
        self.goto(new_x, new_y)
