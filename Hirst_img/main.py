# import colorgram

# colors = colorgram.extract('Hirst_img.jpg', 20)
# rgb_colors = []

# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)

# print(rgb_colors)

color_list =  [(236, 225, 83), (202, 5, 72), (198, 164, 10), (235, 51, 129), (206, 76, 11), (108, 179, 218), (219, 162, 103), (234, 225, 6), (30, 188, 108), (23, 106, 173), (13, 23, 64), (17, 28, 175), (213, 135, 176), (9, 185, 214), (205, 29, 142), (229, 168, 197)]

import turtle as t
import random

tim = t.Turtle()
tim.penup()
tim.hideturtle()
tim.speed(10)
t.colormode(255)

tim.setheading(225)
tim.forward(200)
tim.setheading(0)

for _ in range(10):
    for i in range(10):
        tim.dot(10, random.choice(color_list))
        tim.forward(30)

    tim.setheading(90)
    tim.forward(30)
    tim.setheading(180)
    tim.forward(300)
    tim.setheading(0)

screen = t.Screen()
screen.exitonclick()