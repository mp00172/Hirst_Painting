from turtle import Turtle, Screen
import turtle
import random

turtle.colormode(255)
timmy = Turtle()
timmy.shape("turtle")
directions = [0, 90, 180, 270]


def pick_random_color():
	return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))


def draw_different_shapes():
	for i in range(3, 11):
		timmy.color(pick_random_color())
		for j in range(1, i + 1):
			timmy.forward(100)
			timmy.right(360 / i)


def create_random_walk():
	timmy.pensize(10)
	timmy.speed(10)
	while True:
		timmy.color(pick_random_color())
		timmy.setheading(random.choice(directions))
		timmy.forward(30)


def draw_spirograph(step):
	timmy.speed(0)
	for i in range(360 // step):
		timmy.color(pick_random_color())
		timmy.circle(250)
		timmy.right(step)


# draw_different_shapes()
# create_random_walk()
draw_spirograph(2)


screen = Screen()
screen.exitonclick()