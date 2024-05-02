# Letter Personalization Script

## Overview
This script automates the process of creating personalized letters for a list of invited names. It reads a template letter from `Input/Letters/starting_letter.txt`, replaces the `[name]` placeholder with each name from `Input/Names/invited_names.txt`, and saves the personalized letters in the folder `Output/ReadyToSend/`.

## Features
- Reads a template letter and a list of invited names from text files.
- Replaces placeholders in the letter with actual names.
- Saves personalized letters in a specified output folder.
- Automatically creates the output folder if it doesn't exist.

## Usage
1. Prepare a template letter in `Input/Letters/starting_letter.txt`. Use the placeholder `[name]` where you want to insert the names.
2. Prepare a list of invited names in `Input/Names/invited_names.txt`. Each name should be on a separate line.
3. Run the script.
4. Personalized letters will be created in the `Output/ReadyToSend/` folder.

## Dependencies
- Python 3.x
- No additional dependencies required.

## How to Run
1. Make sure you have Python installed on your system.
2. Clone or download this repository.
3. Navigate to the project directory.
4. Run the script using the following command:
    ```
    main.py
    ```
 ## License

 This project is part of the course: 100 Days of Code: The Complete Python Pro Bootcamp by Dr. Angela Yu, please refere to : https://www.udemy.com/course/100-days-of-code
