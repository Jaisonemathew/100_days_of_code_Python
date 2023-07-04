from turtle import Turtle,Screen
import random

screen = Screen() 
screen.setup(width=500,height=400)
race_on=False
user_bet=screen.textinput(title="Make your bet",prompt="Which turtle will win the race ? Enter a color: ")

colors=["red","green","blue","orange","purple","yellow"]
positions=[-100,-60,-20,20,60,100]
all_turtles=[]

for turtle_index in range(0,6):
    new_turtle= Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.goto(x=-230,y=positions[turtle_index])
    new_turtle.color(colors[turtle_index])
    all_turtles.append(new_turtle)


if user_bet:
    race_on=True

while race_on:
    for turtle in all_turtles:
        if turtle.xcor()>230:
            race_on=False
            winning_color=turtle.pencolor()
            if winning_color==user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
                
        ran_dis = random.randint(0, 10)
        turtle.forward(ran_dis)
    
 

screen.exitonclick()
