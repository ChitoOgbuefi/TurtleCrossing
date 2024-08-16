from turtle import Turtle

STYLE = ("Arial", 15, "normal")


class Level(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.color("black")
        self.penup()
        self.hideturtle()
        self.goto(-260, 210)
        self.update_level()

    def update_level(self):
        self.clear()
        self.write(f"Level: {self.level}", False, "center", STYLE)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", False, "center", STYLE)

    def level_increase(self):
        self.level += 1
        self.update_level()
