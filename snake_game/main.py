from turtle import Screen  # Importing the Screen class for creating the game screen
from snake import Snake  # Importing the Snake class for the game's snake
from food import Food  # Importing the Food class for the game's food
from scoreboard import Scoreboard  # Importing the Scoreboard class for displaying scores
import time  # Importing the time module for pausing the game loop

screen = Screen()  # Creating a screen object for the game
screen.setup(width=600, height=600)  # Setting up the dimensions of the screen
screen.bgcolor("black")  # Setting the background color of the screen to black
screen.title("My Snake Game")  # Setting the title of the game window
screen.tracer(0)  # Turning off animation updates to make the game smoother

snake = Snake()  # Creating a snake object for the game
food = Food()  # Creating a food object for the game
scoreboard = Scoreboard()  # Creating a scoreboard object for the game

screen.listen()  # Listening for keyboard input
screen.onkey(snake.up, "Up")  # Binding the "Up" arrow key to the snake's up method
screen.onkey(snake.down, "Down")  # Binding the "Down" arrow key to the snake's down method
screen.onkey(snake.left, "Left")  # Binding the "Left" arrow key to the snake's left method
screen.onkey(snake.right, "Right")  # Binding the "Right" arrow key to the snake's right method


game_is_on = True  # Variable to control the game loop
while game_is_on:  # Main game loop
    screen.update()  # Updating the screen
    time.sleep(0.1)  # Adding a short delay for smoother gameplay
    snake.move()  # Moving the snake

    # Detect collision with food.
    if snake.head.distance(food) < 15:  # Checking if the snake's head is close to the food
        food.refresh()  # Refreshing the position of the food
        snake.extend()  # Extending the snake
        scoreboard.increase_score()  # Increasing the score

    # Detect collision with wall.
    if (
        snake.head.xcor() > 280
        or snake.head.xcor() < -280
        or snake.head.ycor() > 280
        or snake.head.ycor() < -280
    ):  # Checking if the snake's head hits the wall boundaries
        scoreboard.reset()  # Resetting the scoreboard
        snake.reset()  # Resetting the snake

    # Detect collision with tail.
    for segment in snake.segments[1:]:  # Looping through each segment of the snake
        if snake.head.distance(segment) < 10:  # Checking if the head collides with any segment
            scoreboard.reset()  # Resetting the scoreboard
            snake.reset()  # Resetting the snake

screen.exitonclick()  # Closing the screen when clicked

