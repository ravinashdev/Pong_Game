from turtle import Turtle
class Net(Turtle):
    def __init__(self, screen_height):
        super().__init__()
        self.color("white")
        self.penup()
        self.setposition(0,-300)
        self.setheading(90)
        self.hideturtle()
        self.pensize(10)
        self.screen_height = screen_height
    def draw_line(self):
        for i in range(0,self.screen_height,100):
            self.pendown()
            self.forward(50)
            self.penup()
            self.forward(50)

