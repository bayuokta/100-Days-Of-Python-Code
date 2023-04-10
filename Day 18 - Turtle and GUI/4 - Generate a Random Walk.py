import turtle as t
import random

tim = t.Turtle()
t.colormode(255)


def random_color() -> tuple:
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b


tim.speed('fastest')
tim.pensize(10)
directions = [0, 90, 180, 270]

for _ in range(200):
    tim.color(random_color())
    tim.forward(30)
    tim.setheading(random.choice(directions))
