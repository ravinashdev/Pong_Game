from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, xcor, ycor):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.setposition(xcor,ycor)
    def up(self):
        new_y_coordinate = self.ycor() + 20
        self.setposition(self.xcor(), new_y_coordinate)
    def down(self):
        new_y_coordinate = self.ycor() - 20
        self.setposition(self.xcor(), new_y_coordinate)

