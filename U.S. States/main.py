import turtle
import pandas as pd

#SETTINGS

#general variables
path="C:\\Users\\enman\\Desktop\\Projects\\_U.S. States"
image = f"{path}\\states_img.gif"
df = pd.read_csv(f"{path}\\50_states.csv")
all_states = df.state.to_list()
answers = []
score = 0
msg = "Write a state name:"
playing = True


#turtle
pointer = turtle.Turtle()
pointer.penup()
pointer.hideturtle()

#screen
scr = turtle.Screen()
scr.title("U.S States Game")
scr.addshape(image)
scr.setup(width=725, height=491)
turtle.shape(image)


while playing:
    answer = scr.textinput(title=f"{score}/50 States Correct!", prompt=msg).title()
    
    if answer == "Exit":
        break

    elif answer in answers:
        msg = "You already said that! please give me another answer:"
        
    elif answer in all_states:
        score +=1
        answers.append(answer)
        state_data = df[df.state == answer]
        pointer.goto(int(state_data.x), int(state_data.y))
        pointer.write(answer)



states_to_learn = pd.DataFrame([state for state in all_states if state not in answers])
states_to_learn.to_csv(f"{path}\\States_missed.csv", index=False)
    
