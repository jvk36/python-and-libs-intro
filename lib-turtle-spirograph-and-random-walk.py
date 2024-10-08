import turtle as t
import random


def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return r, g, b


def draw_spirograph(size):
    angle = 0
    for _ in range(360//size):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(angle)
        angle += size


def draw_random_walk():
    directions = [0, 90, 180, 270]
    tim.speed("fastest")
    tim.pen(pensize=10)
    for _ in range(200):
        tim.color(random_color())
        tim.setheading(directions[random.randint(0,3)])
        tim.forward(30)


tim = t.Turtle()
screen = t.Screen()
tim.shape("turtle")
t.colormode(255)
tim.speed("fastest")
draw_spirograph(5)
draw_random_walk()
screen.exitonclick()
