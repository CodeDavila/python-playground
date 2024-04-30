# Import the necessary module
from turtle import Turtle

# Set the distance to move in each step
MOVE_DISTANCE = 10

# Create a Ball class inheriting from Turtle
class Ball(Turtle):
    def __init__(self):
        # Initialize the Turtle object
        super().__init__()
        # Set the shape, color, size, and speed of the ball
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=1, stretch_wid=1)
        self.color("blue")
        self.speed("fastest")
        # Set initial movement in x and y directions
        self.x_move = MOVE_DISTANCE
        self.y_move = MOVE_DISTANCE

    def move(self, speed):
        # Move the ball with the given speed
        new_x = self.xcor() + speed * self.x_move
        new_y = self.ycor() + speed * self.y_move
        self.goto(new_x, new_y)

    def bouncing_y(self):
        # Reverse the y direction when hitting the top or bottom wall
        self.y_move *= -1

    def bouncing_x(self):
        # Reverse the x direction when hitting a paddle
        self.x_move *= -1

    def reset_position(self):
        # Reset the position of the ball to the center and change x direction
        self.goto(0, 0)
        self.bouncing_x()

