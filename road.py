from turtle import Turtle


class Road:

    def __init__(self):
        road_strip = Turtle("square")
        road_strip.color("white")
        road_strip.hideturtle()
        road_strip.penup()
        road_strip.goto(-300, 0)
        road_strip.setheading(0)
        for num in range(300, -300, -20):
            road_strip.pendown()
            road_strip.forward(10)
            road_strip.penup()
            road_strip.forward(10)

        top_grass = Turtle("square")
        top_grass.color("green")
        top_grass.penup()
        top_grass.shapesize(3, 40)
        top_grass.goto(0, 270)

        bot_grass = Turtle("square")
        bot_grass.color("green")
        bot_grass.penup()
        bot_grass.shapesize(3, 40)
        bot_grass.goto(0, -270)




