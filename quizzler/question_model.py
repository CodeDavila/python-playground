class Question:
    """
    A class to represent a single trivia question.

    Attributes:
    - q_text (str): The text of the question.
    - q_answer (str): The answer to the question.
    """

    def __init__(self, q_text, q_answer):
        """
        Initializes a Question object with the provided text and answer.

        Args:
        - q_text (str): The text of the question.
        - q_answer (str): The answer to the question.
        """
        self.text = q_text  # Assigning the question text
        self.answer = q_answer  # Assigning the answer

