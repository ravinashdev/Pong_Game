from turtle import Turtle
BALL_POSITIONS = [(0,0),(20,20),(40,40),(60,60),(80,80),(100,100),(120,120)]

class PongBall(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("blue")
        self.penup()
        self.setposition(0, 0)
        self.x_increment = 20
        self.y_increment = 20
        self.x_coordinate = self.xcor()
        self.y_coordinate = self.ycor()
    def move(self):
        new_y_coordinate = self.ycor() + self.y_increment
        new_x_coordinate = self.xcor() + self.x_increment
        self.setposition(new_x_coordinate, new_y_coordinate)
    def bounce(self):
        self.y_increment*=-1
    def paddle_hit(self):
        self.x_increment*=-1





