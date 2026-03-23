from turtle import Screen
import time
from paddle import Paddle
from pong_ball import PongBall

# Initialize Screen Object
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game Atari")
screen.tracer(0)

# Initialize First Paddle Object
paddle_1 = Paddle(350,0)
# Initialize Second Paddle Object
paddle_2 = Paddle(-350,0)
# Initialize Ball Object
pong_ball = PongBall()
# # Listen for key events to invoke methods to change direction
screen.listen()
screen.onkey(paddle_1.up, "Up")
screen.onkey(paddle_1.down, "Down")
screen.onkey(paddle_2.up, "w")
screen.onkey(paddle_2.down, "s")


# Initialize Game
game_on = True
while game_on:
    pong_ball.move()
    screen.update()
    time.sleep(0.1)
    # Wall Collision
    if abs(pong_ball.ycor()) >= 280:
        pong_ball.bounce()
    # Paddle Collision
    elif abs(pong_ball.xcor()) >= 330 and (pong_ball.distance(paddle_1) < 50 or pong_ball.distance(paddle_2) < 50):
        pong_ball.paddle_hit()

# Screen exit on click
screen.exitonclick()