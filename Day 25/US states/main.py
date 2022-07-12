import turtle

import pandas

screen=turtle.Screen()
screen.title("US state game")
image="blank_states_img.gif"
turtle.addshape(image)
turtle.shape(image)

data=pandas.read_csv("50_states.csv")
all_state=data["state"].to_list()
guessed_state=[]

while len(guessed_state)<50:
    answer_state=screen.textinput(title=f"{len(guessed_state)}/50",prompt="Whats another state's name? ").title()
    print(answer_state)

    if answer_state=="Exit":
        missing_states=[state for state in all_state if state not in guessed_state] #list comprehension
        # missing_states=[]
        # for state in all_state:
        #     if state not in guessed_state:
        #         missing_states.append(state)
        new_data=pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

    if answer_state in all_state:
        guessed_state.append(answer_state)
        t=turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data=data[data.state==answer_state]
        t.goto(int(state_data.x),int(state_data.y))
        t.write(answer_state)


# def get_mouse_click_coor(x,y):
#     print(x,y)

# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()

screen.exitonclick()