from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("purple")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move(self):
        self.goto(self.xcor() + self.x_move, self.ycor() + self.y_move)

    def increase_speed(self):
        self.move_speed *= 0.9  # smaller means faster as move_speed determines the time to sleep in the main loop

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1

    def reset_position(self):
        self.x_move *= -1
        self.goto(0, 0)
        self.move_speed = 0.1
