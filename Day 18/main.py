# import colorgram
# rgb_colors=[]
# colors = colorgram.extract("image.jpg",30)
# for i in colors:
#     r=i.rgb.r
#     g=i.rgb.g
#     b=i.rgb.b
#     new_color=(r,g,b)
#     rgb_colors.append(new_color)
# print(rgb_colors)

import turtle as turtle_module 
import random

tim=turtle_module.Turtle()
turtle_module.colormode(255)
tim.speed("fastest")
tim.penup()
tim.hideturtle()
color_list=[(246, 243, 237), (248, 242, 245), (240, 246, 241), (200, 167, 110), (237, 241, 246), (144, 74, 52), (169, 152, 45), (58, 92, 119), (224, 203, 131), (136, 162, 180), (131, 34, 26), (51, 117, 89), (199, 94, 72), (143, 25, 30), (18, 97, 74), (69, 47, 40), (173, 146, 153), (150, 177, 152), (131, 70, 74), (56, 43, 46), (237, 174, 163), (184, 88, 94), (38, 58, 71), (28, 82, 89), (182, 204, 178), (242, 156, 160), (93, 144, 124), (20, 66, 57), (36, 65, 96), (108, 125, 154)]

tim.setheading(225)
tim.forward(250)
tim.setheading(0)
num_of_dots=100

for i in range(1,num_of_dots+1):
    tim.dot(20,random.choice(color_list))
    tim.forward(50)

    if i%10==0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen=turtle_module.Screen()
screen.exitonclick()