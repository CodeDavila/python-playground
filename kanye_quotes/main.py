# Import necessary modules
from tkinter import *
import requests

# Function to request a Kanye West quote from the API
def request_quote():
    response = requests.get(url="https://api.kanye.rest/")  # Send GET request to the API
    response.raise_for_status()  # Raise an exception for any HTTP error that occurred during the request

    data = response.json()  # Convert response to JSON format
    return data["quote"]  # Extract and return the quote from the JSON data

# Function to update the displayed quote on the canvas
def get_quote():
    quote = request_quote()  # Call the function to get a new quote
    canvas.itemconfig(quote_text, text=quote)  # Update the text displayed on the canvas with the new quote

# Create main window
window = Tk()
window.title("Kanye Says...")  # Set window title
window.config(padx=50, pady=50)  # Set padding for the window

# Create canvas for displaying the quote and background image
canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file="background.png")
canvas.create_image(150, 207, image=background_img)  # Display background image
quote_text = canvas.create_text(150, 207, text=request_quote(), width=250, font=("Arial", 20, "bold"), fill="white")
# Display initial quote text on canvas
canvas.grid(row=0, column=0)  # Add canvas to the window

# Create button to get a new quote
kanye_img = PhotoImage(file="kanye.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)  # Add button to the window

window.mainloop()  # Start the event loop

