from turtle import Turtle
import turtle
import pandas

#------------------UI------------------
FONT = ("Courier", 8, "bold")
screen = turtle.Screen()
screen.title("U.S States Game")
img = "blank_states_img.gif"
screen.addshape(img)
turtle.shape(img)

#------------------FETCH CSV DATA------------------
name_data = "50_states.csv"
# get only the columns you want from the csv file
df = pandas.read_csv("50_states.csv", usecols=['state', 'x', 'y'])
dict_state = df.to_dict(orient='records')
# print(dict_state)

#------------------GAME------------------
correct_answer = []
score = 0
while len(correct_answer) < 50:
    if score == 0:
        answer_state = screen.textinput(title="Guess the state", prompt="What's another state's name?")
    elif score > 0:
        answer_state = screen.textinput(title=f"{score}/50 States Correct", prompt="What's another state's name?")
    if score >= 0 and answer_state == 'exit':
        break
    titled_answer = answer_state.title()
    for state in dict_state:
        if state['state'] == titled_answer:
            state_coordinate = Turtle()
            state_coordinate.hideturtle()
            state_coordinate.penup()
            state_coordinate.goto(x=state['x'], y=state['y'])
            state_coordinate.write(f"{state['state']}", align="center", font=FONT)
            correct_answer.append(state['state'])
            score = len(correct_answer)


#------------------SAVE INCORRECT STATES NAMES TO CSV FILE------------------
# learn = []
# for item in dict_state:
#     if item['state'] not in correct_answer:
#         learn.append(item['state'])

#list comprehension
learn = [item['state'] for item in dict_state if item['state'] not in correct_answer]
data_dict = {
    "state": learn
}
df = pandas.DataFrame(data_dict)
df.to_csv("states_to_learn.csv")

# keep screen open click
turtle.mainloop()
#
# my approach was to make a dictionary to access each items; state, x and y
# angela fetched all the values that are matching with state name.
#
# # state_data = data[data.state == answer_state]
# # int(state_data.x) int(state_data.y)