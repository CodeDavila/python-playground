# Import necessary modules
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

# Define coordinates for paddles
RIGHT = (350, 0)
LEFT = (-350, 0)

# Initial game settings
GAME = 7
SPEED = 1

# Set up the screen
screen = Screen()
screen.setup(width=800, height=600)
screen.title("Pong")
screen.bgcolor("Black")
screen.tracer(0)

# Create paddles, ball, and scoreboards
r_paddle = Paddle(RIGHT)
l_paddle = Paddle(LEFT)
ball = Ball()
scoreboard_l = Scoreboard(1, -200)
scoreboard_r = Scoreboard(2,  200)

# Listen for key inputs
screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")

# Main game loop
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    ball.move(SPEED)

    # Check if ball hits top or bottom wall and change direction
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bouncing_y()
    
    # Check if ball hits paddle and change direction
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 320) or (ball.distance(l_paddle) < 50 and ball.xcor() < -320):
        ball.bouncing_x()
    
    # Check if ball passes the paddles and reset position, increase score, and speed
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard_l.increase_score(1)
        SPEED += 0.2
    elif ball.xcor() < -380:
        ball.reset_position()
        scoreboard_r.increase_score(2)
        SPEED += 0.2
    
    # Check if any player wins the game
    if scoreboard_l.score == GAME:
        game_is_on = False
        scoreboard_l.game_over(1)
    elif scoreboard_r.score == GAME:
        game_is_on = False
        scoreboard_l.game_over(2)

# Close the game window when clicked
screen.exitonclick()

