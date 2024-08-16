from cars import Cars
from player import Player
from turtle import Screen, Turtle
from road import Road
from level import Level
import time

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("dark grey")
screen.title("Turtle Crossing")
screen.tracer(0)

game_map = Road()
player1 = Player()
cars = Cars()
level2 = Level()

screen.listen()

screen.onkey(key = "Up", fun = player1.up)


game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars.create_car()
    cars.move(level2.level)
    for car in cars.all_cars:
        if player1.distance(car) <= 15:
            game_is_on = False
    if player1.ycor() > 270:
        player1.goto(0, -270)
        level2.level_increase()


level2.game_over()

screen.exitonclick()








screen.exitonclick()