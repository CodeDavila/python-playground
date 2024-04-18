import random
from .constants import *

# Star class
class Star:
    def __init__(self):
        """
        Initializes a Star object with random coordinates and depth.
        """
        self.x = random.randint(-CANVAS_WIDTH // 2, CANVAS_WIDTH // 2)
        self.y = random.randint(-CANVAS_HEIGHT // 2, CANVAS_HEIGHT // 2)
        self.depth = random.randint(1, max(CANVAS_WIDTH, CANVAS_HEIGHT))
        self.prev_depth = self.depth

    def update(self, speed):
        """
        Updates the position of the star based on the given speed.
        
        Args:
            speed (int): The speed at which the star moves.
        """
        self.depth -= speed
        if self.depth < 1:
            self.reset_star()

    def reset_star(self):
        """
        Resets the position and depth of the star to random values.
        """
        self.depth = max(CANVAS_WIDTH, CANVAS_HEIGHT)
        self.x = random.randint(-CANVAS_WIDTH // 2, CANVAS_WIDTH // 2)
        self.y = random.randint(-CANVAS_HEIGHT // 2, CANVAS_HEIGHT // 2)
        self.prev_depth = self.depth

    def calculate_screen_coordinates(self):
        """
        Calculates the screen coordinates of the star based on its depth.
        
        Returns:
            tuple: A tuple containing the previous and current screen coordinates,
                   as well as the stroke width.
        """
        screen_x = self.map_value(self.x / self.depth, -0.5, 0.5, 0, CANVAS_WIDTH)
        screen_y = self.map_value(self.y / self.depth, -0.5, 0.5, 0, CANVAS_HEIGHT)
        prev_screen_x = self.map_value(self.x / self.prev_depth, -0.5, 0.5, 0, CANVAS_WIDTH)
        prev_screen_y = self.map_value(self.y / self.prev_depth, -0.5, 0.5, 0, CANVAS_HEIGHT)
        self.prev_depth = self.depth
        stroke_width = self.map_value(self.depth, 0, max(CANVAS_WIDTH, CANVAS_HEIGHT), 4, 0)
        return prev_screen_x, prev_screen_y, screen_x, screen_y, stroke_width

    @staticmethod
    def map_value(value, in_min, in_max, out_min, out_max):
        """
        Maps a value from one range to another.
        
        Args:
            value (float): The value to be mapped.
            in_min (float): Minimum value of the input range.
            in_max (float): Maximum value of the input range.
            out_min (float): Minimum value of the output range.
            out_max (float): Maximum value of the output range.
            
        Returns:
            float: The mapped value.
        """
        return (value - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

