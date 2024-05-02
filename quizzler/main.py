# Importing necessary modules and classes
from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from ui import QuizzInterface

# Creating a list to store Question objects
question_bank = []

# Iterating through the question data to create Question objects
for question in question_data:
    question_text = question["question"]  # Extracting question text
    question_answer = question["correct_answer"]  # Extracting correct answer
    new_question = Question(question_text, question_answer)  # Creating Question object
    question_bank.append(new_question)  # Adding Question object to the list

# Creating a QuizBrain object with the list of questions
quiz = QuizBrain(question_bank)

# Creating a QuizzInterface object to start the quiz
quiz_ui = QuizzInterface(quiz)

