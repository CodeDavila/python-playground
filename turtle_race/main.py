# Import necessary modules
import random
import turtle
from turtle import Turtle, Screen

# Create a screen object
screen = Screen()

# Set up the screen dimensions
screen.setup(width=500, height=400)

# Prompt the user to make a bet on the winning turtle
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? ENTER A COLOR: ")

# Define the colors and starting positions for each turtle
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]

# Create turtles and set their initial positions
all_turtles = []
for turtle_index in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

# Flag to control the race
is_race_on = False

# If the user has made a bet, start the race
if user_bet:
    is_race_on = True

# Race loop
while is_race_on:
    # Move each turtle forward in random distances
    for turtle in all_turtles:
        # Check if any turtle has reached the finish line
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            # Check if the winning turtle matches the user's bet and print the result
            if winning_color == user_bet:
                print("You win!")
            else:
                print("You lose")
        
        # Move the turtle forward by a random distance
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

# Close the screen when clicked
screen.exitonclick()

