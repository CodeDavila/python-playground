import time  # Importing the time module for adding delays
from turtle import Screen  # Importing the Screen class from the turtle module
from player import Player  # Importing the Player class from the player module
from car_manager import CarManager  # Importing the CarManager class from the car_manager module
from scoreboard import Scoreboard  # Importing the Scoreboard class from the scoreboard module

# Setting up the screen
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)  # Turn off automatic screen updates

# Creating player, car manager, and scoreboard objects
mikey = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

# Listening for keyboard inputs
screen.listen()
screen.onkey(mikey.up, "Up")  # Assigning the "Up" key to move the player turtle up
screen.onkey(mikey.down, "Down")  # Assigning the "Down" key to move the player turtle down

game_is_on = True  # Variable to control the game loop
while game_is_on:
    time.sleep(0.1)  # Adding a small delay for smoother gameplay
    screen.update()  # Updating the screen manually
    car_manager.create_cars()  # Creating new cars
    car_manager.move_cars()  # Moving the cars
    if mikey.refresh():  # Checking if the player turtle has crossed the finish line
        scoreboard.increase_score()  # Increasing the score
        car_manager.increment_speed()  # Increasing the speed of the cars
        car_manager.car_chance -= 2  # Increasing the likelihood of new cars
    for car in car_manager.all_cars:
        if car.distance(mikey) < 40:  # Checking for collision between cars and the player turtle
            game_is_on = False  # Ending the game loop if collision occurs
            scoreboard.game_over()  # Displaying "GAME OVER" message

screen.exitonclick()  # Closing the screen when clicked

