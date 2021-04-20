# import colorgram

# rgb_colors = []
# colors = colorgram.extract('image.jpg', 50)

# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)

# print(rgb_colors)
color_list = [(111, 167, 210), (208, 174, 4), (27, 117, 170), (247, 209, 0), (197, 218, 233), (144, 166, 154), (60, 124, 75), (204, 138, 179), (233, 198, 217), (221, 156, 88), (246, 219, 63), (178, 89, 17), (229, 222, 205), (144, 16, 86), (158, 56, 111), (82, 5, 54), (224, 171, 198), (216, 222, 219), (10, 107, 32), (78, 162, 67), (186, 91, 141), (9, 58, 84), (156, 192, 235), (72, 132, 193), (9, 66, 25), (43, 153, 194), (87, 27, 6), (167, 199, 212), (141, 31, 9), (208, 95, 67), (96, 94, 6), (22, 80, 96), (170, 205, 166), (233, 173, 160), (19, 66, 119)]

# 10 * 10 rows of spots
# dots should be 20 in size, and spaced by 50 spaces

import turtle as turtle_module
import random

turtle_module.colormode(255)
turtle = turtle_module.Turtle()
turtle.speed("fastest")
turtle.penup()
turtle.hideturtle()

turtle.setheading(180)
turtle.forward(225)
turtle.setheading(270)
turtle.forward(220)
turtle.setheading(0)

for lines in range(10):
    for dot_count in range(10):
        turtle.dot(20, random.choice(color_list))
        turtle.forward(50)
    turtle.setheading(90)
    turtle.forward(50)
    turtle.setheading(180)
    turtle.forward(500)
    turtle.setheading(0)

screen = turtle.Screen()
screen.exitonclick()