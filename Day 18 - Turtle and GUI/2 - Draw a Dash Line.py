from turtle import Turtle, Screen


turtle = Turtle()
for i in range(15):
    turtle.forward(15)
    turtle.penup()
    turtle.forward(15)
    turtle.pendown()

screen = Screen()
screen.exitonclick()
