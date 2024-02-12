import turtle
import pandas


screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
game_is_on = True
score = 0
correct_guesses = []

while len(correct_guesses) < 50:
    answer_state = screen.textinput(title=f"{score}/50 States Correct", prompt="What's another state's name?").title()
    state_list = pandas.read_csv("50_states.csv")
    all_states = state_list.state.tolist()
    if answer_state == "Exit":
        missed_states = []
        for state in all_states:
            if state not in correct_guesses:
                missed_states.append(state)
        new_data = pandas.DataFrame(missed_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in all_states and answer_state not in correct_guesses:
        correct_guesses.append(answer_state)
        score += 1
        tim = turtle.Turtle()
        tim.penup()
        tim.hideturtle()
        answer_row = state_list[state_list.state == answer_state]
        state_x = int(answer_row.x)
        state_y = int(answer_row.y)
        tim.goto(state_x, state_y)
        tim.write(answer_state)








