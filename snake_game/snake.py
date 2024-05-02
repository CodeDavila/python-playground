from turtle import Turtle  # Importing the Turtle class for creating graphical elements

# Constants for snake starting positions, movement distance, and directions
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]  # Initial positions for snake segments
MOVE_DISTANCE = 20  # Distance to move in each step
UP = 90  # Angle to move the snake upwards
DOWN = 270  # Angle to move the snake downwards
LEFT = 180  # Angle to move the snake leftwards
RIGHT = 0  # Angle to move the snake rightwards

class Snake:
    def __init__(self):
        self.segments = []  # List to hold the segments of the snake
        self.create_snake()  # Creating the initial snake
        self.head = self.segments[0]  # The head of the snake is the first segment
        self.head.color("green")  # Setting the color of the snake's head

    def create_snake(self):  # Method to create the snake segments
        for position in STARTING_POSITIONS:  # Loop through starting positions
            self.add_segment(position)  # Add a segment at each starting position

    def reset(self):  # Method to reset the snake to its initial state
        for seg in self.segments:  # Loop through all segments
            seg.goto(1000, 1000)  # Move the segment off-screen
        self.segments.clear()  # Clear the list of segments
        self.create_snake()  # Recreate the snake
        self.head = self.segments[0]  # Set the head to the first segment
        self.head.color("green")  # Set the color of the head

    def add_segment(self, position):  # Method to add a new segment to the snake
        new_segment = Turtle("square")  # Creating a new segment as a square
        new_segment.color("white")  # Setting the color of the segment
        new_segment.penup()  # Pen up to prevent drawing lines when moving
        new_segment.goto(position)  # Moving the segment to the specified position
        self.segments.append(new_segment)  # Adding the segment to the list of segments

    def extend(self):  # Method to extend the length of the snake
        self.add_segment(self.segments[-1].position())  # Adding a new segment at the last segment's position

    def move(self):  # Method to move the snake forward
        for seg_num in range(len(self.segments) - 1, 0, -1):  # Loop through segments starting from the end
            new_x = self.segments[seg_num - 1].xcor()  # Get the x-coordinate of the segment before
            new_y = self.segments[seg_num - 1].ycor()  # Get the y-coordinate of the segment before
            self.segments[seg_num].goto(new_x, new_y)  # Move the current segment to the position of the segment before
        self.head.forward(MOVE_DISTANCE)  # Move the head forward by the defined distance

    def up(self):  # Method to move the snake upwards
        if self.head.heading() != DOWN:  # Check if the snake is not already moving downwards
            self.head.setheading(UP)  # Set the direction of the head upwards

    def down(self):  # Method to move the snake downwards
        if self.head.heading() != UP:  # Check if the snake is not already moving upwards
            self.head.setheading(DOWN)  # Set the direction of the head downwards

    def left(self):  # Method to move the snake leftwards
        if self.head.heading() != RIGHT:  # Check if the snake is not already moving rightwards
            self.head.setheading(LEFT)  # Set the direction of the head leftwards

    def right(self):  # Method to move the snake rightwards
        if self.head.heading() != LEFT:  # Check if the snake is not already moving leftwards
            self.head.setheading(RIGHT)  # Set the direction of the head rightwards

