import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. state Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


data = pandas.read_csv("50_states.csv")
us_states = data['state'].tolist()
print(us_states)

guessed_state = []

while len(guessed_state) < len(us_states):
    answer_state = screen.textinput(title=f"{len(guessed_state)}/{len(us_states)}",  prompt="What's another state name").title()
    #answer_state = answer_state.title()

    if answer_state == "Exit":
        missing_state = [state for state in us_states if state not in guessed_state]
        #for state in us_states:
            #if state not in guessed_state:
               #missing_state.append(state)
        new_data = pandas.DataFrame(missing_state)
        new_data.to_csv("state_to_learn.csv")
        break

    if answer_state in us_states:
        if answer_state not in guessed_state:
            guessed_state.append(answer_state)
            state_data = data[data.state == answer_state]
            t = turtle.Turtle()
            t.hideturtle()
            t.penup()
            x = int(state_data.x)
            y = int(state_data.y)
            t.goto(x, y)
            t.write(answer_state, align="center", font=("Arial", 8, "normal"))



# is_game_on = True
# correct_list =[]
# while is_game_on:
#     answer_state = screen.textinput(title="Guess the state", prompt="What's another state name")
#     answer_state = answer_state.title()
#     print(answer_state)
#     data = pandas.read_csv("50_states.csv")
#     is_state_found = data['state'] == answer_state
#     if is_state_found.any():
#
#         correct_list.append(answer_state)
#         score = len(correct_list)
#         correct_answer = data[data['state'] == answer_state]
#         print(data[data['state'] == answer_state])
#         x = int(correct_answer['x'])
#         y = int(correct_answer['y'])
#         turtle.goto(x, y)
#         turtle.penup()
#         turtle.write(answer_state)
#



