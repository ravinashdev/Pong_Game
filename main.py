from turtle import Screen
import time
from paddle import Paddle
from pong_ball import PongBall
from score_board import ScoreBoard

# Initialize Screen Object
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game Atari")
screen.tracer(0)

# Initialize First Paddle Object (Right)
paddle_1 = Paddle(350,0)
# Initialize Second Paddle Object (Left)
paddle_2 = Paddle(-350,0)
# Initialize Ball Object
pong_ball = PongBall()
# Initialize ScoreBoard for each player
paddle_1_score = ScoreBoard(x_coordinate= 175,y_coordinate= 200)
paddle_2_score = ScoreBoard(x_coordinate= -175, y_coordinate=200)
paddle_1_score.write_score()
paddle_2_score.write_score()

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
        pong_ball.y_inverse()
    # Paddle Collision using abs value of paddle position and 50 pixels from paddle
    elif abs(pong_ball.xcor()) >= 320 and (pong_ball.distance(paddle_1) < 50 or pong_ball.distance(paddle_2) < 50):
        pong_ball.x_inverse()
        # pong_ball.ball_speed_increase()
    # PongBall passes any of the paddles and reset
    elif abs(pong_ball.xcor()) >= 350:
        # Logic to increase scoreboard respectively as it passes the paddle of one player
        if pong_ball.xcor() > 350:
            paddle_2_score.increase_score()
            paddle_2_score.write_score()
        elif pong_ball.xcor() < -340:
            paddle_1_score.increase_score()
            paddle_1_score.write_score()
        pong_ball.reset_position()
# Screen exit on click
screen.exitonclick()