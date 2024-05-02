import turtle  # Import the turtle module for graphics
import pandas  # Import pandas for data manipulation

# Create a screen for the game
screen = turtle.Screen()
screen.title("U.S States Game")

# Load the image of the U.S. map
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# Create a turtle to mark guessed states
marker = turtle.Turtle()

# Load the data of U.S. states from a CSV file
data = pandas.read_csv("50_states.csv")
states = data.state.to_list()  # Get a list of all state names

guessed_states = []  # List to keep track of guessed states

# Continue the game until all states are guessed or user cancels
while len(guessed_states) < 50:  # There are 50 states in total
    # Prompt the user to guess a state
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                    prompt="What's another state's name?")
    
    # Exit loop if user cancels
    if answer_state is None:
        break
    
    answer_state = answer_state.title()  # Capitalize the first letter of each word

    # Check if the guessed state is correct and not already guessed
    if answer_state in states and answer_state not in guessed_states:
        guessed_states.append(answer_state)  # Add the guessed state to the list
        state_data = data[data.state == answer_state].iloc[0]  # Get data of the guessed state
        x = state_data.x
        y = state_data.y
        marker.penup()
        marker.goto(x, y)
        marker.write(answer_state, align="center", font=("Courier", 10, "normal"))

# Create a CSV file with the missed states if user exits
missed_states = [state for state in states if state not in guessed_states]
missed_states_data = pandas.DataFrame(missed_states, columns=["Missed States"])
missed_states_data.to_csv("missed_states.csv", index=False)

# Close the screen when clicked
screen.exitonclick()

