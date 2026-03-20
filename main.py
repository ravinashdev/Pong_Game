from turtle import Screen
import time
from paddle import Paddle

# Initialize Screen Object
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game Atari")
screen.tracer(0)

# Initialize First Paddle
paddle_1 = Paddle(350,0)
# Initialize Second Paddle
paddle_2 = Paddle(-350,0)

# # Listen for key events to invoke methods to change direction
screen.listen()
screen.onkey(paddle_1.up, "Up")
screen.onkey(paddle_1.down, "Down")
screen.onkey(paddle_2.up, "w")
screen.onkey(paddle_2.down, "s")


# Initialize Game
game_on = True
while game_on:
    screen.update()
    time.sleep(0.05)
# Screen exit on click
screen.exitonclick()