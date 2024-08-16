from turtle import Turtle
import random

CAR_COLORS = ["green", "blue", "yellow", "black", "purple", "orange", "red", "black", "cyan"]
SIDE = [-320, 320]
MAP_RANGE = list(range(-220, -20)) + list(range(20, 220))
MOVE_INCREMENT = 10
STARTING_MOVE_DISTANCE = 5


class Cars:
    def __init__(self):
        self.all_cars = []

    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(1, 2)
            new_car.penup()
            new_car.color(random.choice(CAR_COLORS))
            y_placement = random.choice(MAP_RANGE)
            if y_placement >= 20:
                new_car.goto(-320, y_placement)
                new_car.setheading(0)
            if y_placement <= -20:
                new_car.goto(320, y_placement)
                new_car.setheading(180)
            self.all_cars.append(new_car)

    def move(self, level):
        for car in self.all_cars:
            car.forward(self.speed_increase(level))

    def speed_increase(self, level):
        return STARTING_MOVE_DISTANCE * level









