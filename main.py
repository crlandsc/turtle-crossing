# Import modules
import random
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# initialize screen
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)  # only update screen when called to update

# initialize objects
cars = CarManager()
player = Player()
scoreboard = Scoreboard((-280, 250))

# screen object to listen for key input
screen.listen()
screen.onkeypress(fun=player.move, key="Up")

# initialize variables
car_speed = 0
car_refresh = 1
random_interval = 10

# begin game
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars.move(car_speed)  # move each car per update

    player_position = player.position()
    # cars.delete_car()
    car_refresh += 1

    if car_refresh % random_interval == 0:
        random_interval = random.randint(1, 20)
        cars.generate_car()

    # if goal (top of screen) reached, reset player position, speed up cars, add point to scoreboard
    if player_position[1] > 280:
        player.reset_position()
        scoreboard.increase_level()
        car_speed += 5

    # Determine if turtle collision with cars
    cars.call_car_positions()  # update all car positions
    for current_position in cars.car_positions:
        car_x_coord = current_position[0]  # determine if car is close to turtle on x-axis
        y_collision = current_position[1] - player_position[1]  # determine if car is close to turtle on y axis
        if -20 < car_x_coord < 20 and -20 < y_collision < 20:
            scoreboard.game_over()
            game_is_on = False


screen.exitonclick()
