from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
CAR_LENGTH = 2


class CarManager:
    def __init__(self):
        self.cars = []
        self.car_positions = []
        self.generate_car()
        self.game_is_on = True

    def generate_car(self):
        new_car = Turtle(shape="square")
        new_car.color(random.choice(COLORS))
        new_car.turtlesize(stretch_wid=1, stretch_len=CAR_LENGTH)
        new_car.speed(0)
        new_car.penup()
        new_car.setheading(180)
        starting_position = (280, random.randint(-250, 250))
        new_car.setposition(starting_position)
        self.cars.append(new_car)

    def move(self, car_speed):
        for car in self.cars:
            car.forward(MOVE_INCREMENT + car_speed)

    def call_car_positions(self):
        self.car_positions = []
        for car in self.cars:
            self.car_positions.append(car.position())

    # Didn't get to work. Not necessary, just trying to be efficient on space
    # def delete_car(self):
    #     for car in self.cars:
    #         current_car_position = car.position()
    #         if current_car_position[0] < -10:
    #             car.clear()
