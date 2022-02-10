import colorgram
import turtle
from turtle import Turtle, Screen
import random

# Extract 40 colors from an image.
# colors = colorgram.extract('artimage.jpg', 40)

# # colorgram.extract returns Color objects, which let you access
# # RGB, HSL, and what proportion of the image was that color.
# first_color = colors[0]
# rgb = first_color.rgb # e.g. (255, 151, 210)
# hsl = first_color.hsl # e.g. (230, 255, 203)
# proportion  = first_color.proportion # e.g. 0.34
# list_col =[]
# for color in colors:
#     list_col.append((color.rgb.r,color.rgb.g,color.rgb.b))
# print(list_col)

## Saved the extracted image colors in a list
color_list = [(232, 251, 242), (198, 12, 32), (250, 237, 17), (39, 76, 189), (38, 217, 68), (238, 227, 5), (229, 159, 46), (27, 40, 157), (215, 74, 12), (15, 154, 16), (199, 14, 10), (242, 246, 252), (243, 33, 165), (229, 17, 121), (73, 9, 31), (60, 14, 8), (224, 141, 211), (10, 97, 61), (221, 160, 9), (17, 18, 43), (46, 214, 232), (11, 227, 239), (81, 73, 214), (238, 156, 220), (74, 213, 167), (77, 234, 202), (52, 234, 243), (3, 67, 40), (218, 87, 49), (174, 178, 231), (237, 169, 164), (6, 245, 223), (247, 9, 42), (10, 79, 112), (16, 54, 243), (240, 16, 16)]

turtle.colormode(255)
def random_color():
    tup = color_list[random.randint(0,l)]
    return(tup)



tim = Turtle()
l= len(color_list)
print(tim.xcor())
print(tim.ycor())
tim.hideturtle()
tim.penup()
tim.forward(-300)
tim.right(90)
tim.forward(300)
tim.left(90)
for j in range(10):
    for i in range(10):
        tim.pendown()
        tup = color_list[random.randint(0,l-1)]
        # print(tup)
        tim.pencolor(tup)
        # tim.showturtle()
        tim.speed(6)
        tim.dot(20)
        tim.penup()
        tim.fd(50)
    # tim.hideturtle()
    tim.speed(0)
    tim.forward(-500)
    tim.left(90)
    tim.fd(50)
    tim.right(90)


screen= Screen()
screen.exitonclick()