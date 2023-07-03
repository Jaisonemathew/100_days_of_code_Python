import turtle as t
import random
tim=t.Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()
t.colormode(255)
color_list=[(249, 232, 19),(110, 195, 66), (199, 12, 31), (195, 67, 21), (213, 13, 9),(226, 55, 3), (55, 41, 63),(32, 91, 188), (234, 151, 39), (232, 229, 5)]

tim.setheading(225)
tim.forward(300)
tim.setheading(0)
dot_num=100
for dot in range(1,dot_num+1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)
    if dot%10==0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

t.exitonclick()
