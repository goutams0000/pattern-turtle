import turtle
from turtle import Turtle, Screen
from random import randint

timmy = Turtle()
timmy.shape('turtle')
timmy.color('coral')
turtle.colormode(255)


def set_colour():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    return (r, g, b)

timmy.speed('fastest')
for i in range(3, 11):
    timmy.color(set_colour())
    for j in range(i):
        timmy.forward(100)
        turning_angle = 360 / i
        timmy.right(turning_angle)

screen = Screen()
screen.exitonclick()
