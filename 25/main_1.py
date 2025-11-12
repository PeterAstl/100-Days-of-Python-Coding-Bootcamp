
from turtle import Screen, Turtle
from Maptext import State
import pandas
from pandas.core.interchange.from_dataframe import primitive_column_to_ndarray

screen = Screen()
screen.title("US States")
image = "blank_states_img.gif"
screen.addshape(image)
t = Turtle()

t.shape(image)

correct = "Guess the State"
score = 0

answer_state = screen.textinput(title=correct, prompt= "Whats another state's name")
answer_state = answer_state.title()
print(answer_state)

states = pandas.read_csv("50_states.csv")
states_list = states["state"].tolist()

while answer_state in states_list:
    if answer_state == "exit":
        break
    score += 1
    correct = f"{score}/50 States Correct"
    current_state = State()
    data = states.loc[states["state"] == answer_state]
    ycor= data["y"].iloc[0]
    xcor = data["x"].iloc[0]
    current_state.write_state(answer_state, xcor, ycor)
    states_list.remove(answer_state)
    answer_state = screen.textinput(title=correct, prompt= "Whats another state's name")
    answer_state = answer_state.title()


print(f"your final score is {score}/50")
new_highscore = pandas.DataFrame(states_list)
new_highscore.to_csv("to_learn.csv")
screen.exitonclick()

# with open(f"./record", "w") as highscore:
#     highscore.write(f"{states_list}")


screen.exitonclick()


# def get_mouse_click_coor(x, y):
#     print(x, y)
#
# screen.onscreenclick(get_mouse_click_coor)
#
# screen.mainloop()