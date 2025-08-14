
# from turtle import Turtle, Screen
# import colorgram
# tim = Turtle()
# tim.shape("turtle")
# tim.color("red")
#
# for _ in range(20):
#     tim.forward(10)
#     if _ % 2 == 0:
#         tim.penup()
#     else:
#         tim.pendown()
# # tim.right(90)
# #
# #
# screen = Screen()
# screen.exitonclick()

# from turtle import *
# import turtle as t
#
# tim = t.Turtle()
#
# import heroes
# print(heroes.gen())

# import colorgram
# rgb_colors = []
# colors = colorgram.extract("HirstDots.jpg", 10)
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
# print(rgb_colors)

import turtle as turtle_module
import random
turtle_module.colormode(255)

tim = turtle_module.Turtle()
color_list = [(235, 37, 113), (143, 26, 67), (237, 72, 37), (220, 164, 55), (15, 140, 88), (174, 162, 50)]
tim.speed("fastest")
tim.penup()
tim.hideturtle()
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen = turtle_module.Screen()
screen.exitonclick()



