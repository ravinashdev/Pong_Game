from turtle import Turtle
class PongBall(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("blue")
        self.penup()
        self.shapesize(stretch_wid=2, stretch_len=2)
        self.setposition(0, 0)