import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S State Game")
img = "blank_states_img.gif"
screen.addshape(img)
turtle.shape(img)

data = pandas.read_csv("50_states.csv")
all_states = data['state'].to_list()
guest_state = []

while len(guest_state) < 50:
    answer_state = screen.textinput(title=f'{len(guest_state)} State Correct',
                                    prompt='What\'s another state\'s name').title()

    if answer_state == 'Exit':
        break
    if answer_state in all_states:
        guest_state.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data['state'] == answer_state]
        t.goto(int(state_data['x'].item()), int(state_data['y'].item()))
        t.write(state_data['state'].item())


# states_to_learn.csv
all_states = [state for state in all_states if state not in guest_state]
state_to_learn = pandas.DataFrame(all_states)
state_to_learn.columns = ['state']
state_to_learn.to_csv('states_to_learn.csv')
