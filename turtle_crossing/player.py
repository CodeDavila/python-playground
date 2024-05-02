from turtle import Turtle  # Importing the Turtle module for creating graphics

STARTING_POSITION = (0, -260)  # Initial position of the player turtle
MOVE_DISTANCE = 10  # Distance the player turtle moves in each step
FINISH_LINE_Y = 260  # Y-coordinate of the finish line


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")  # Set the shape of the player turtle to "turtle"
        self.color("orange", "green")  # Set the color of the player turtle
        self.shapesize(stretch_wid=2, stretch_len=2)  # Stretch the turtle shape
        self.setheading(90)  # Set the orientation of the turtle to face upwards
        self.penup()  # Lift the pen to prevent drawing lines
        self.goto(STARTING_POSITION)  # Move the turtle to the starting position

    def up(self):
        """
        Method to move the player turtle upwards.
        """
        self.forward(MOVE_DISTANCE)  # Move the turtle forward by MOVE_DISTANCE pixels

    def down(self):
        """
        Method to move the player turtle downwards.
        """
        self.backward(MOVE_DISTANCE)  # Move the turtle backward by MOVE_DISTANCE pixels

    def refresh(self):
        """
        Method to check if the player turtle has reached the finish line.
        If reached, move the turtle back to the starting position.
        """
        if self.ycor() >= FINISH_LINE_Y:  # Check if the turtle's y-coordinate is beyond the finish line
            self.goto(STARTING_POSITION)  # Move the turtle back to the starting position
            return True  # Return True to indicate that the turtle has crossed the finish line
        return False  # Return False if the turtle has not crossed the finish line

