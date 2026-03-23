from turtle import Screen
import time
from paddle import Paddle
from pong_ball import PongBall
from score_board import ScoreBoard
from net import Net

# Initialize Screen Object
screen = Screen()
screen_width = 800
screen_height = 600
screen.setup(screen_width, screen_height)
screen.bgcolor("black")
screen.title("Pong Game Atari")
screen.tracer(0)

# Initialize First Paddle Object (Right)
paddle_1 = Paddle(350,0)
# Initialize Second Paddle Object (Left)
paddle_2 = Paddle(-350,0)
# Initialize Ball Object
pong_ball = PongBall()
# Initialize Net line
net = Net(screen_height)
net.draw_line()
# Initialize ScoreBoard for each player with a starting score of 0
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
    # PongBall passes any of the paddles one player scores and the ball resets
    elif abs(pong_ball.xcor()) >= 350:
        # Logic to increase scoreboard respectively as it passes the paddle of one player
        if pong_ball.xcor() > 350:
            paddle_2_score.increase_score()
            paddle_2_score.write_score()
        elif pong_ball.xcor() < -350:
            paddle_1_score.increase_score()
            paddle_1_score.write_score()
        pong_ball.reset_position()
    # Game over condition for when the first paddle 1 reach's 11
    elif (paddle_1_score.score or paddle_2_score.score) == 11:
        game_over = ScoreBoard(x_coordinate= 0,y_coordinate= 0)
        net.clear()
        # Logic to display the winning player on screen with GAME OVER!
        if paddle_1_score.score == 11:
            winner = "Player 1 Wins!"
        elif paddle_2_score.score == 11:
            winner = "Player 2 Wins!"
        game_over.game_over(winner)
        game_on = False
# Screen exit on click
screen.exitonclick()