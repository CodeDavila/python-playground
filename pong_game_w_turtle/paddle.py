# Import the necessary module
from turtle import Turtle

# Set the distance to move in each step
MOVE_DISTANCE = 50

# Create a Paddle class inheriting from Turtle
class Paddle(Turtle):
    def __init__(self, position):
        # Initialize the Turtle object
        super().__init__()
        # Set the shape, color, size, and position of the paddle
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(position)

    def up(self):
        # Move the paddle up by MOVE_DISTANCE
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(x=self.xcor(), y=new_y)

    def down(self):
        # Move the paddle down by MOVE_DISTANCE
        new_y = self.ycor() - MOVE_DISTANCE
        self.goto(x=self.xcor(), y=new_y)

