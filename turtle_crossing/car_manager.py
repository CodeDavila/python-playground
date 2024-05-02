from turtle import Turtle  # Importing the Turtle module for creating graphics
import random  # Importing the random module for generating random numbers

# List of colors for the cars
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
# Initial distance the cars move at each step
STARTING_MOVE_DISTANCE = 5
# Distance increment when speed increases
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.all_cars = []  # List to store all the created cars
        self.move_distance = STARTING_MOVE_DISTANCE  # Initial distance moved by each car
        self.car_chance = 10  # Likelihood of a new car being created

    def create_cars(self):
        """
        Method to create new cars.
        """
        # Randomly determine whether to create a new car based on car_chance
        random_chance = random.randint(1, self.car_chance)
        if random_chance == 1:  # If random_chance equals 1, create a new car
            new_car = Turtle("square")  # Create a new car object
            new_car.shapesize(stretch_wid=2, stretch_len=3)  # Set the size of the car
            new_car.penup()  # Lift the pen to prevent drawing lines
            new_car.color(random.choice(COLORS))  # Set a random color for the car
            random_y = random.randint(-220, 230)  # Generate a random y-coordinate for the car
            new_car.goto(300, random_y)  # Move the car to the starting position on the right side of the screen
            self.all_cars.append(new_car)  # Add the new car to the list of all cars

    def move_cars(self):
        """
        Method to move all the cars to the left.
        """
        # Move each car in the list backwards (to the left) by move_distance pixels
        for car in self.all_cars:
            car.backward(self.move_distance)

    def increment_speed(self):
        """
        Method to increase the speed of the cars.
        """
        # Increase the move_distance by MOVE_INCREMENT to speed up the cars
        self.move_distance += MOVE_INCREMENT

