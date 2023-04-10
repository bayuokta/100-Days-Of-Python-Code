import random
from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=500, height=400)
y_position = [-70, -40, -10, 20, 50, 80]
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
user_bet = screen.textinput(title='Make your bet', prompt='Which turtle will win the race ? Enter a color ?')
all_turtle = []
is_race_on = False


for turtle_index in range(0, 6):
    new_turtle = Turtle(shape='turtle')
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_position[turtle_index])
    all_turtle.append(new_turtle)

if user_bet:
    is_race_on = True


while is_race_on:
    for turtle in all_turtle:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if user_bet == winning_color:
                print(f'You\'ve won!. The {winning_color} turtle is the winner!')
            else:
                print(f'You\'ve lost!. The {winning_color} turtle is the winner!')
        turtle.forward(random.randint(0, 10))



screen.exitonclick()