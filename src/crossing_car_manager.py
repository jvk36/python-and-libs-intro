from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        super().__init__()
        self.cars = []
        self.move_distance = STARTING_MOVE_DISTANCE

    def add_car(self):
        # add a car once every 6 times or so this method is called
        choice = random.randint(1, 6)
        if choice == 1:
            car = Turtle()
            car.shape("square")
            car.penup()
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.color(COLORS[random.randint(0, len(COLORS)-1)])
            car.goto(280, random.randint(-250, 250))
            self.cars.append(car)

    def increase_speed(self):
        self.move_distance += MOVE_INCREMENT

    def move_all_cars(self):
        for car in self.cars:
            car.goto(car.xcor()-self.move_distance, car.ycor())