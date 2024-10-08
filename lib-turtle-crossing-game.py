import time
from turtle import Screen
from src.crossing_player import Player
from src.crossing_car_manager import CarManager
from src.crossing_scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(player.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.add_car()
    car_manager.move_all_cars()

    # handle collision
    for car in car_manager.cars:
        if player.distance(car) < 20:
            game_is_on = False
            scoreboard.game_over()

    # handle turtle reaching destination
    if player.have_crossed():
        player.reset_position()
        car_manager.increase_speed()
        scoreboard.update_score()

screen.exitonclick()
