from tkinter import *  # Importing the necessary modules
import math

# ---------------------------- CONSTANTS ------------------------------- #

# Constants for colors and timing intervals
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
REPS = 0  # Tracking the number of repetitions
CHECK_TEXT = ""  # Tracking the checkmarks
TIMER = ""  # Timer variable

# ---------------------------- TIMER RESET ------------------------------- #

# Function to reset the timer
def reset_timer():
    global REPS, CHECK_TEXT, TIMER  # Accessing global variables
    window.after_cancel(TIMER)  # Cancelling the timer
    REPS = 0  # Resetting repetitions
    CHECK_TEXT = ""  # Resetting checkmarks
    label_checkmark.config(text=CHECK_TEXT)  # Updating checkmark label
    label_title.config(text="Timer", fg=GREEN)  # Updating title label
    canvas.itemconfig(timer_text, text="00:00")  # Resetting timer display

# ---------------------------- TIMER MECHANISM ------------------------------- #

# Function to start the timer
def start_timer():
    global REPS  # Accessing global variable
    REPS += 1  # Incrementing repetitions
    work_sec = WORK_MIN * 60  # Converting work minutes to seconds
    short_break_sec = SHORT_BREAK_MIN * 60  # Converting short break minutes to seconds
    long_break_sec = LONG_BREAK_MIN * 60  # Converting long break minutes to seconds

    if REPS % 8 == 0:  # Long break after every 8 repetitions
        label_title.config(text="Long Break", fg=RED)  # Updating title label
        count_down(long_break_sec)  # Starting countdown for long break
    elif REPS % 2 == 0:  # Short break after every 2 repetitions
        label_title.config(text="Short Break", fg=PINK)  # Updating title label
        count_down(short_break_sec)  # Starting countdown for short break
    else:
        label_title.config(text="Work", fg=GREEN)  # Updating title label
        count_down(work_sec)  # Starting countdown for work

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

# Function for countdown mechanism
def count_down(count):
    global CHECK_TEXT, TIMER  # Accessing global variables
    count_min = math.floor(count/60)  # Calculating minutes
    count_sec = count % 60  # Calculating seconds
    if count_sec < 10:
        count_sec = f"0{count_sec}"  # Formatting seconds to have leading zero if less than 10
    count_text = f"{count_min}:{count_sec}"  # Formatting the countdown text

    canvas.itemconfig(timer_text, text=count_text)  # Updating timer display
    if count > 0:
        TIMER = window.after(1000, count_down, count-1)  # Recursively calling count_down after 1 second
    else:
        start_timer()  # Starting the timer again after countdown finishes
        if REPS % 2 == 0:
            CHECK_TEXT += "✔"  # Adding checkmark for completed work session
            label_checkmark.config(text=CHECK_TEXT)  # Updating checkmark label

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()  # Creating Tkinter window
window.title("Pomodoro")  # Setting window title
window.config(padx=100, pady=50, bg=YELLOW)  # Setting window padding and background color

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)  # Creating canvas for tomato image
tomato_img = PhotoImage(file="tomato.png")  # Loading tomato image
canvas.create_image(100, 112, image=tomato_img)  # Placing tomato image on canvas
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 25, "bold"))  # Creating timer text on canvas
canvas.grid(row=1, column=1)  # Placing canvas on window grid

label_title = Label(text="Timer", fg=GREEN, font=(FONT_NAME, 30, "bold"), bg=YELLOW)  # Creating title label
label_title.grid(row=0, column=1)  # Placing title label on window grid

label_checkmark = Label(text=CHECK_TEXT, fg=GREEN, font=(FONT_NAME, 20, "bold"), bg=YELLOW)  # Creating checkmark label
label_checkmark.grid(row=3, column=1)  # Placing checkmark label on window grid

button_start = Button(text="Start", font=(FONT_NAME, 15, "bold"), command=start_timer, highlightbackground=YELLOW)  # Creating start button
button_start.grid(row=2, column=0)  # Placing start button on window grid

button_reset = Button(text="Reset",font=(FONT_NAME, 15, "bold"), command=reset_timer, highlightbackground=YELLOW)  # Creating reset button
button_reset.grid(row=2, column=2)  # Placing reset button on window grid

window.mainloop()  # Running the main event loop

