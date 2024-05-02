import html

class QuizBrain:
    """
    A class to manage the quiz and its questions.

    Attributes:
    - question_number (int): The current question number.
    - score (int): The player's score.
    - question_list (list): List of Question objects representing the quiz questions.
    - current_question (Question): The current question being asked.
    """

    def __init__(self, q_list):
        """
        Initializes a QuizBrain object with the provided list of questions.

        Args:
        - q_list (list): List of Question objects representing the quiz questions.
        """
        self.question_number = 0  # Initializing the question number
        self.score = 0  # Initializing the score
        self.question_list = q_list  # Assigning the list of questions
        self.current_question = None  # Initializing the current question

    def still_has_questions(self):
        """
        Checks if there are still questions left in the quiz.

        Returns:
        - bool: True if there are more questions, False otherwise.
        """
        return self.question_number < len(self.question_list)

    def next_question(self):
        """
        Gets the next question from the question list and formats it.

        Returns:
        - str: The formatted text of the next question.
        """
        self.current_question = self.question_list[self.question_number]  # Getting the current question
        self.question_number += 1  # Incrementing the question number
        q_text = html.unescape(self.current_question.text)  # Unescaping HTML entities in question text
        return f"Q.{self.question_number}: {q_text}"

    def check_answer(self, user_answer):
        """
        Checks if the user's answer is correct and updates the score accordingly.

        Args:
        - user_answer (str): The user's answer to the current question.

        Returns:
        - bool: True if the answer is correct, False otherwise.
        """
        correct_answer = self.current_question.answer  # Getting the correct answer
        if user_answer.lower() == correct_answer.lower():  # Checking if the answer is correct
            self.score += 1  # Incrementing the score if the answer is correct
            return True
        else:
            return False

