from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which title would win? type a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []
y_pos = -100
for c in colors:
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(c)
    new_turtle.penup()
    new_turtle.goto(-238, y_pos)
    y_pos += 50
    all_turtles.append(new_turtle)

race_is_on = True
while race_is_on:
    for t in all_turtles:
        t.forward(random.randint(0, 10))
        if t.xcor() >= 230:
            race_is_on = False
            winning_color = t.pencolor()
            if user_bet == winning_color:
                print(f"You won. The winning turtle was the {winning_color} one!")
            else:
                print(f"You lost. The winning turtle was the {winning_color} one!")


screen.exitonclick()
