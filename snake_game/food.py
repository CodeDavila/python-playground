from turtle import Turtle  # Importing the Turtle class for creating graphical elements
import random  # Importing the random module for generating random numbers

class Food(Turtle):  # Creating a Food class which inherits from the Turtle class

    def __init__(self):  # Constructor method to initialize a Food object
        super().__init__()  # Calling the constructor of the parent class
        self.shape("circle")  # Setting the shape of the food to a circle
        self.penup()  # Pen up to prevent drawing lines when moving
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)  # Stretching the circle to make it look like a square
        self.color("blue")  # Setting the color of the food to blue
        self.speed("fastest")  # Setting the speed of the food movement to the fastest possible
        self.refresh()  # Calling the refresh method to position the food randomly

    def refresh(self):  # Method to refresh the position of the food
        random_x = random.randint(-250, 250)  # Generating a random x-coordinate within a specific range
        random_y = random.randint(-250, 250)  # Generating a random y-coordinate within a specific range
        self.goto(random_x, random_y)  # Moving the food to the randomly generated position

