import turtle as t
import random

tim=t.Turtle()
tim.shape("turtle")
t.colormode(255)
tim.speed("fastest")

def random_color():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    random_color=(r,g,b)
    return random_color


# def draw_shape(num_sides):
#     angle=360/num_sides
#     for _ in range(num_sides):
#         tim.forward(100)
#         tim.right(angle)
# for i in range(3,11):
#     draw_shape(i)


# directions=[0,90,180,270]
# tim.pensize(15)

# for _ in range(200):
#     tim.color(random_color())
#     tim.forward(30)
#     tim.setheading(random.choice(directions))


def draw_spirograph(size_of_gap):
    for _ in range(int(360/size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading()+size_of_gap)

draw_spirograph(5)

screen=t.Screen()
screen.exitonclick()