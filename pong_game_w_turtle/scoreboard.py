# Import the necessary module
from turtle import Turtle

# Set alignment and font for scoreboard
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")

# Create a Scoreboard class inheriting from Turtle
class Scoreboard(Turtle):
    def __init__(self, player, x_pos):
        # Initialize the Turtle object
        super().__init__()
        # Set initial score to zero and configure scoreboard appearance
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(x_pos, 260)
        self.hideturtle()
        # Update the scoreboard with the initial player score
        self.update_scoreboard(player)

    def update_scoreboard(self, player):
        # Update the scoreboard with the current score
        self.write(f"Player {player}: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self, player):
        # Display game over message with the winning player
        self.goto(0, 0)
        self.write(f"   GAME OVER \nPlayer {player}. Wins!", align=ALIGNMENT, font=FONT)

    def increase_score(self, player):
        # Increment the score and update the scoreboard
        self.score += 1
        self.clear()
        self.update_scoreboard(player)

