import tkinter as tk
import pygame
import random
from modules.constants import *
from modules.stars import *

def animate():
    """
    Animates the simulation by updating the position of stars on the canvas.
    """
    canvas.delete('all')
    for star in stars:
        star.update(speed)
        properties = star.calculate_screen_coordinates()
        random_color = random.choice(SHADES_OF_COLORS)
        canvas.create_line(*properties[0:4], fill=random_color, width=properties[-1])
    window.after(FRAME_DELAY, animate)

def place_kirk_image():
    """
    Places Captain Kirk's image on the canvas.
    """
    enterprise_image_label.place_forget()
    kirk_image_label.place(x=CANVAS_WIDTH + 10, y=WINDOW_HEIGHT - kirk_image_label.winfo_reqheight() - 10)

def change_speed(value):
    """
    Changes the speed of the animation based on the slider value and updates Captain's message.

    Args:
        value (int): The value of the slider representing the speed.
    """
    global speed
    speed = int(value)
    captain_kirk = ""
    if 30 <= speed <= 50:
        captain_kirk = "Scotty,\nwe need more power!"
        place_kirk_image()
    elif 100 <= speed <= 120:
        captain_kirk = "Mr. Sulu,\nbring us up to warp speed."
        place_kirk_image()
    elif speed == 200:
        captain_kirk = "Mr. Sulu,\ntake us out of warp !!!"
        place_kirk_image()
    else:
        kirk_image_label.place_forget()
        enterprise_image_label.place(x=CANVAS_WIDTH + 10, y=WINDOW_HEIGHT - enterprise_image_label.winfo_reqheight() - 10)
    captain_message.config(text=captain_kirk)

# Main window
window = tk.Tk()
window.title("Warp Speed")
window.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")
window.resizable(False, False)
window.configure(bg='black')
window.attributes('-alpha', 0.90)

# Music player
music_file = "resources/music/opening.mp3"
pygame.mixer.init()
pygame.mixer.music.load(music_file)
pygame.mixer.music.play(-1)

# Canvas for animation
canvas = tk.Canvas(window, width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg='black')
canvas.pack(side=tk.LEFT)

# Speed control slider
speed_control = tk.Scale(window, from_=10, to=200, orient='vertical', command=change_speed)
speed_control.place(x=CANVAS_WIDTH + (150 - speed_control.winfo_reqwidth()) // 2, y=(WINDOW_HEIGHT - speed_control.winfo_reqheight()) // 2)

# Label for speed control
label_text = "Warp\nSpeed"
label = tk.Label(window, text=label_text, font=("Courier", 16), bg="white", fg="red")
label.place(x=CANVAS_WIDTH + (150 - label.winfo_reqwidth()) // 2, y=CANVAS_HEIGHT // 2 - speed_control.winfo_reqheight())

# Stars
stars = [Star() for _ in range(3000)]

# Load and display Enterprise image
enterprise_image_path = "resources/images/enterprise.png"
enterprise_image = tk.PhotoImage(file=enterprise_image_path).subsample(8, 8)
enterprise_image_label = tk.Label(window, image=enterprise_image, bg="black")
enterprise_image_label.place(x=CANVAS_WIDTH + 10, y=WINDOW_HEIGHT - enterprise_image_label.winfo_reqheight() - 10)

# Load and display Captain Kirk's image
kirk_image_path = "resources/images/captain-kirk.png"
kirk_image = tk.PhotoImage(file=kirk_image_path).subsample(3, 3)
kirk_image_label = tk.Label(window, image=kirk_image, bg="black")
kirk_image_label.place_forget()

# Label for Captain's message
captain_message = tk.Label(window, text="", font=("Courier", 20), bg="black", fg="orange")
captain_message.place(x=CANVAS_WIDTH // 2, y=WINDOW_HEIGHT - kirk_image_label.winfo_reqheight() // 2)

# Initialize speed
speed = 10

# Start main event loop
animate()
window.mainloop()

