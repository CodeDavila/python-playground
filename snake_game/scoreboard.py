from turtle import Turtle  # Importing the Turtle class for creating graphical elements

# Constants for scoreboard alignment and font
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):  # Creating a Scoreboard class which inherits from the Turtle class

    def __init__(self):  # Constructor method to initialize a Scoreboard object
        super().__init__()  # Calling the constructor of the parent class
        self.score = 0  # Initializing the score to 0
        self.high_score = 0  # Initializing the high score to 0
        self.color("white")  # Setting the color of the scoreboard text to white
        self.penup()  # Pen up to prevent drawing lines when moving
        self.goto(0, 260)  # Positioning the scoreboard at the specified coordinates
        self.hideturtle()  # Hiding the turtle icon
        self.high_score_read()  # Reading the high score from a file
        self.update_scoreboard()  # Updating the scoreboard with the current score and high score

    def high_score_read(self):  # Method to read the high score from a file
        with open("high_score.txt", mode="r") as file:  # Opening the file in read mode
            self.high_score = int(file.read())  # Reading the high score and converting it to an integer

    def high_score_write(self):  # Method to write the high score to a file
        with open("high_score.txt", mode="w") as file:  # Opening the file in write mode
            file.write(str(self.high_score))  # Writing the high score to the file and converting it to a string

    def update_scoreboard(self):  # Method to update the scoreboard with the current score and high score
        self.clear()  # Clearing the previous content of the scoreboard
        # Writing the current score and high score to the scoreboard
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):  # Method to reset the score and update the scoreboard
        if self.score > self.high_score:  # Checking if the current score is higher than the high score
            self.high_score = self.score  # Updating the high score if the current score is higher
        self.score = 0  # Resetting the score to 0
        self.update_scoreboard()  # Updating the scoreboard with the reset score and high score
        self.high_score_write()  # Writing the high score to a file

    def game_over(self):  # Method to display "GAME OVER" on the scoreboard
        self.goto(0, 0)  # Moving the turtle to the center of the screen
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)  # Writing "GAME OVER" on the scoreboard

    def increase_score(self):  # Method to increase the score by 1 and update the scoreboard
        self.score += 1  # Increasing the score by 1
        self.update_scoreboard()  # Updating the scoreboard with the new score

