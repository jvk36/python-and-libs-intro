from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=-0.5)
        self.color("blue")
        self.refresh()

    def refresh(self):
        food_pos_x = random.randint(-280, 280)
        food_pos_y = random.randint(-280, 280)
        self.goto(food_pos_x, food_pos_y)
