from turtle import Turtle
from random import randint, choice

class CarManager:
    def __init__(self):
        # Declare variables
        self.COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
        self.STARTING_MOVE_DISTANCE = 5
        self.MOVE_INCREMENT = 5
        self.car_speed = self.STARTING_MOVE_DISTANCE
        self.all_cars = []


    def create_car(self):
        # Create turtle car
        random_chance = randint(1,6)
        if random_chance == 1:
            car = Turtle()
            car.shape('square')
            car.penup()
            car.shapesize(1,2)
            car.color(choice(self.COLORS))
            car.goto(280, randint(-250, 250))
            self.all_cars.append(car)

    def move_car(self):
        # Move the all cars by 10 pixels
        for car in self.all_cars:
            car.backward(self.car_speed)

    def speed_up(self):
        # Increase cars movement speed
        self.car_speed += self.MOVE_INCREMENT

    def restart(self):
        # Revert back to normal speed of cars
        self.car_speed = self.STARTING_MOVE_DISTANCE




