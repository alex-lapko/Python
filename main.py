import colorgram
import os
import turtle
import random

# Get absolute path of current script's directory
current_dir = os.path.dirname(os.path.abspath(__file__))
image_path = os.path.join(current_dir, 'image.jpg')

rgb_colors = []
colors = colorgram.extract(image_path, 30)
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb_colors.append(new_color)

print(rgb_colors)

turtle.colormode(255)
turtle = turtle.Turtle()
screen = turtle.getscreen()

turtle.hideturtle()
turtle.speed("fastest")

turtle.penup()
vertical = -200
turtle.sety(vertical)

for i in range(10):
    turtle.setx(-200)
    for j in range(10):
        turtle.dot(20, random.choice(rgb_colors))
        turtle.forward(50)
    vertical += 50
    turtle.sety(vertical)

screen.exitonclick()



