# import colorgram

# colors = colorgram.extract("image.jpg", 30)  # Extract colors from an image
# rgb_colors = []
# for color in colors:
#    r = color.rgb.r
#    g = color.rgb.g
#    b = color.rgb.b
#    new_color = (r, g, b)
#    rgb_colors.append(new_color)

import turtle as turtle_module
import random

# RGB colors extracted from the image or any other source
colors = [(233, 233, 232), (231, 233, 237), (236, 231, 233), (224, 233, 227), (207, 160, 82),
          (54, 88, 130), (145, 91, 40), (140, 26, 49), (221, 207, 105), (132, 177, 203),
          (158, 46, 83), (45, 55, 104), (169, 160, 39), (129, 189, 143), (83, 20, 44),
          (37, 43, 67), (186, 94, 107), (187, 140, 170), (85, 120, 180), (59, 39, 31),
          (88, 157, 92), (78, 153, 165), (194, 79, 73), (45, 74, 78), (80, 74, 44),
          (161, 201, 218), (57, 125, 121), (219, 175, 187), (169, 206, 172), (219, 182, 169)]

# Setup Turtle graphics
turtle_module.colormode(255)
tim = turtle_module.Turtle()
tim.speed("fastest")
tim.hideturtle()
tim.penup()
tim.setheading(225)
tim.forward(300)
tim.setheading(0)

num_of_dots = 101
for dot_count in range(1, num_of_dots):
    # Draw dots with random colors from the provided color list
    tim.dot(20, random.choice(colors))
    tim.forward(50)
    if dot_count % 10 == 0:
        # Move to the next row after every 10 dots
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

# Close the turtle graphics window when clicked
screen = turtle_module.Screen()
screen.exitonclick()

