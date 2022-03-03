import colorgram
import turtle
import random

OFFSET_X = 25
OFFSET_Y = 8


def color_list(ec):
	cl = []
	for i in range(len(ec)):
		tup = (ec[i].rgb.r, ec[i].rgb.g, ec[i].rgb.b)
		cl.append(tup)
	return cl


extracted_colors = colorgram.extract("color_palette_image.jpg", 20)
available_colors = color_list(extracted_colors)

turtle.colormode(255)
dot = turtle.Turtle()
screen = turtle.Screen()

dot.pensize(20)
dot.speed(0)
dot.penup()
dot.sety(-(screen.window_height() // 2) + OFFSET_Y)
while dot.ycor() < screen.window_height() // 2:
	dot.setx(-(screen.window_width() // 2) + OFFSET_X)
	dot.sety(dot.ycor() + 60)
	while dot.xcor() < screen.window_width() // 2:
		dot.color(random.choice(available_colors))
		dot.pendown()
		dot.forward(1)
		dot.penup()
		dot.forward(60)
screen.exitonclick()

