from turtle import Turtle,Screen
tim= Turtle()
screen = Screen() 

def move_forward():
    tim.forward(10)

def move_back():
    tim.backward(10)

def move_left():
    tim.left(10)

def move_right():
    tim.right(10)

def clears():
    tim.home()
    tim.clear()
    


screen.listen()
screen.onkey(key="w",fun=move_forward)
screen.onkey(key="s",fun=move_back)
screen.onkey(key="a",fun=move_left)
screen.onkey(key="d",fun=move_right)
screen.onkey(key="c",fun=clears)


screen.exitonclick()
