import turtle
import random

# OFFICIAL TUTORIALS AT https://docs.python.org/3/library/turtle.html

# CREATING A TURTLE

# Create a screen object
screen = turtle.Screen()

# Create a turtle object
t = turtle.Turtle()

# Draw a line
t.forward(100)  # Move the turtle forward by 100 units

# CHANGING THE TURTLE's PROPERTIES

# Change the color of the turtle
t.color("blue")

# Change the turtle's pen size
t.pensize(3)

# Change the turtle's speed
t.speed(1)  # Slowest
t.left(45)
t.forward(100)

# DRAW SHAPES

# Draw a square
for _ in range(4):
    t.forward(100)
    t.right(90)

# Draw a circle pattern
for _ in range(36):
    t.forward(10)
    t.right(10)  # Turn right by 10 degrees

# Draw a star
for _ in range(5):
    t.forward(100)
    t.right(144)  # Turn right by 144 degrees

# Filling shapes with color
# Begin filling color
t.begin_fill()
t.color("red")

# Draw a shape
for _ in range(4):
    t.forward(100)
    t.right(90)

# End filling color
t.end_fill()

# Drawing Spirals
for i in range(100):
    t.forward(i)
    t.right(10)

# Draw a spiral with random colors
for i in range(360):
    t.forward(i)
    t.right(59)
    t.pencolor(random.random(), random.random(), random.random())  # Set random color

# CHANGING THE BACKGROUND COLOR AND WINDOW TITLE
# Set the background color
screen.bgcolor("lightgreen")

# Set the window title
screen.title("Turtle Drawing")


# t.screen is an instance of the Screen that a Turtle instance exists on; 
# it’s created automatically along with the turtle.
screen.mainloop()
