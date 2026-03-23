from turtle import Turtle

class PongBall(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(stretch_wid=2, stretch_len=2)
        self.color("blue")
        self.penup()
        self.setposition(0, 0)
        self.x_increment = 20
        self.y_increment = 20
        self.x_coordinate = self.xcor()
        self.y_coordinate = self.ycor()
        self.speed = 1
    def move(self):
        new_y_coordinate = self.ycor() + self.y_increment
        new_x_coordinate = self.xcor() + self.x_increment
        self.setposition(new_x_coordinate, new_y_coordinate)
    def y_inverse(self):
        self.y_increment*=-1
    def x_inverse(self):
        self.x_increment*=-1
    def reset_position(self):
        # Reset ball to center and the winner gets the first hit
        self.setposition(0, 0)
        self.y_inverse()
        self.x_inverse()
    def ball_speed_increase(self):
        self.speed +=1
        print(self.speed)






