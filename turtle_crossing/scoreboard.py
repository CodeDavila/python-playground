from turtle import Turtle  # Importing the Turtle module for creating graphics

# Font style for the scoreboard
FONT = ("Courier", 24, "normal")
# Alignment of the text in the scoreboard
ALIGNMENT = "center"


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0  # Initial score
        self.color("black")  # Set the color of the scoreboard text to black
        self.penup()  # Lift the pen to prevent drawing lines
        self.goto(-100, 260)  # Move the scoreboard to the specified position
        self.hideturtle()  # Hide the turtle icon
        self.update_scoreboard()  # Update the scoreboard with the initial score

    def update_scoreboard(self):
        """
        Method to update the scoreboard with the current score.
        """
        # Write the score on the screen with specified alignment and font
        self.write(f"Level: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        """
        Method to display "GAME OVER" message.
        """
        self.goto(0, 0)  # Move the turtle to the center of the screen
        # Write "GAME OVER" on the screen with specified alignment and font
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        """
        Method to increase the score by 1 and update the scoreboard.
        """
        self.score += 1  # Increment the score by 1
        self.clear()  # Clear the previous scoreboard
        self.update_scoreboard()  # Update the scoreboard with the new score

