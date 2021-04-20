import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()

while len(all_states) != 0:
    answer = screen.textinput(
        title=f"{50 - len(all_states)}/50 States Correct",
        prompt="What's another state's name?",
    ).title()

    if answer == "Exit":
        missed_states = pandas.DataFrame(all_states)
        missed_states.to_csv("states_to_learn.csv")
        break

    if answer in all_states:
        all_states.remove(answer)
        writer = turtle.Turtle()
        writer.hideturtle()
        writer.penup()
        state_data = data[data.state == answer]
        writer.goto(int(state_data.x), int(state_data.y))
        writer.write(f"{answer}", True, align="center")
