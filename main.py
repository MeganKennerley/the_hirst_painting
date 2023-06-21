import random
import turtle
from turtle import Turtle, Screen

tim = Turtle()
turtle.colormode(255)
tim.penup()
tim.speed("fastest")
tim.hideturtle()

color_list = [(56, 108, 149), (226, 132, 55), (197, 145, 172), (234, 201, 101), (145, 81, 54), (140, 180, 207), (233, 225, 195), (138, 130, 73)]

def draw_dots():
    i = 0
    x = -250
    y = -250
    while i < 10:
        tim.setx(x)
        tim.sety(y)
        for _ in range(0, 10):
            tim.dot(20, random.choice(color_list))
            tim.forward(50)
        i += 1
        y += 50


draw_dots()


screen = Screen()
screen.exitonclick()
