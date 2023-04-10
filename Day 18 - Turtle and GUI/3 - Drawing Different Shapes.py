from turtle import Turtle, Screen


triangle = Turtle()
for _ in range(3):
    triangle.forward(100)
    triangle.right(120)

square = Turtle()
square.color('blue')
for _ in range(4):
    square.forward(100)
    square.right(90)

pentagon = Turtle()
pentagon.color('red')
for _ in range(5):
    pentagon.forward(100)
    pentagon.right(72)

hexagon = Turtle()
hexagon.color('green')
for _ in range(6):
    hexagon.forward(100)
    hexagon.right(60)

heptagon = Turtle()
heptagon.color('aquamarine3')
for _ in range(7):
    heptagon.forward(100)
    heptagon.right((360/7))

octagon = Turtle()
octagon.color('bisque3')
for _ in range(8):
    octagon.forward(100)
    octagon.right((360/8))

nonagon = Turtle()
nonagon.color('brown3')
for _ in range(9):
    nonagon.forward(100)
    nonagon.right((360/9))

decagon = Turtle()
decagon.color('CadetBlue3')
for _ in range(10):
    decagon.forward(100)
    decagon.right((360/10))


screen = Screen()
screen.exitonclick()
