from turtle import Turtle, Screen
import random

tim = Turtle()
colors = ['cornflower blue', 'cyan', 'medium spring green', 'green', 'green yellow', 'yellow green', 'gold', 'tan',
          'saddle brown', 'orange red']


def draw_shape(num_side: int):
    angle = 360 / num_side
    for _ in range(num_side):
        tim.forward(100)
        tim.right(angle)


for i in range(3, 11):
    tim.color(random.choice(colors))
    draw_shape(i)

screen = Screen()
screen.exitonclick()
