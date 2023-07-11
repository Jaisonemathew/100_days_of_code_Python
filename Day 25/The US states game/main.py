import turtle
import pandas as pd
screen=turtle.Screen()
screen.title("U.S States Game")
image="blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
count=0
data=pd.read_csv("50_states.csv")
ans=[]

while(len(ans)<50):
    answer_state=screen.textinput(title=f"{count}/50 States Correct",prompt="What's another state's name?").title()
    if answer_state=="Exit":
        missing_states=[]
        for state in list(data.state):
             if state not in ans:
                 missing_states.append(state)
        new_data=pd.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    for state in list(data.state):
     if answer_state==state:
            count+=1
            ans.append(answer_state)
            t = turtle.Turtle()
            t.hideturtle()
            t.penup()
            state_data=data[data.state==answer_state]
            x = int(state_data.x.item())
            y = int(state_data.y.item())
            t.goto(x, y)
            t.write(state_data.state.item())
            

turtle.mainloop()