from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
import time

screen = Screen()
screen.tracer(0)

screen.bgcolor("black")
screen.setup(width=800,height=600)
screen.title("Pong")

r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
ball = Ball((0,0))

screen.listen()
screen.onkeypress(r_paddle.go_up,"Up")
screen.onkeypress(r_paddle.go_down,"Down")
screen.onkeypress(l_paddle.go_up,"w")
screen.onkeypress(l_paddle.go_down,"s")

game_on = True

while game_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

screen.exitonclick()