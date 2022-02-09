import turtle
from turtle import Turtle, Screen
import random
#new Turtle object
tim = Turtle()
#tim.color("red")
#tim.pensize(5)
turtle.colormode(255)
def random_color():
    r= random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return((r,g,b))

# directions =[0,90,180,270,360]
tim.speed(0)
# for i in range(500):
#     tim.pencolor(random_color())
#     tim.forward(30)
#     k = random.randint(0,3)
#     tim.setheading(directions[k])

initial=tim.heading()

def draw(a):
    for i in range(int(360/a)):
        tim.pencolor(random_color())
        tim.circle(radius = 100)
        tim.setheading(tim.heading() + a)

draw(10)

screen= Screen()
screen.exitonclick()