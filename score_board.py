from turtle import Turtle
MOVE = False
ALIGN = "center"
FONT = ("Courier", 30, "bold")
class ScoreBoard(Turtle):
    def __init__(self, x_coordinate, y_coordinate):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.setposition(x_coordinate, y_coordinate)
    def write_score(self):
        # Write Score on Screen
        self.write(self.score, MOVE, ALIGN, FONT)
    def increase_score(self):
        # Increase the score everytime ball passes a paddle
        self.score += 1
        # Clear the screen so new score can get written when it's incremented by 1'
        self.clear()
    def game_over(self):
        message = f"Game Over!"
        self.setposition(0,0)
        self.write(message, MOVE, ALIGN, font=("Courier", 32, "bold"))