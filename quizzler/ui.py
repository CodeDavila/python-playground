from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizzInterface:
    """
    A class to represent the graphical user interface for the quiz.

    Attributes:
    - quiz (QuizBrain): The QuizBrain object managing the quiz.
    - window (Tk): The main window of the interface.
    - score_label (Label): Label displaying the current score.
    - canvas (Canvas): Canvas displaying the quiz questions.
    - question_text (int): Identifier for the text displayed on the canvas.
    - false_button (Button): Button for selecting 'False' answer.
    - true_button (Button): Button for selecting 'True' answer.
    """

    def __init__(self, quiz_brain: QuizBrain):
        """
        Initializes the QuizzInterface with the provided QuizBrain object.

        Args:
        - quiz_brain (QuizBrain): The QuizBrain object managing the quiz.
        """
        self.quiz = quiz_brain  # Assigning the QuizBrain object
        self.window = Tk()  # Creating the main window
        self.window.title("Quizzler")  # Setting the window title
        self.window.config(bg=THEME_COLOR, pady=20, padx=20)  # Configuring window background and padding

        # Creating and placing the score label
        self.score_label = Label(text=f"Score: {self.quiz.score}", font=("Arial", 15, "italic"))
        self.score_label.config(fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        # Creating and placing the canvas for displaying questions
        self.canvas = Canvas(width=300, height=250, bg="black", highlightthickness=0)
        self.question_text = self.canvas.create_text(150, 125, width=280, text="", font=("Arial", 20, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        # Creating and placing the 'False' button
        false_image = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_image, highlightthickness=0, command=self.check_false)
        self.false_button.grid(row=2, column=0)

        # Creating and placing the 'True' button
        true_image = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_image, highlightthickness=0, command=self.check_true)
        self.true_button.grid(row=2, column=1)

        # Getting the first question
        self.get_next_question()

        # Running the main event loop
        self.window.mainloop()

    def get_next_question(self):
        """
        Retrieves and displays the next question from the QuizBrain object.
        """
        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.question_text, text=q_text)
        self.score_label.config(text=f"Score: {self.quiz.score}", font=("Arial", 15, "italic"))

    def still_has_questions(self):
        """
        Checks if there are still questions remaining in the quiz.
        """
        self.canvas.config(bg="black")
        if self.quiz.still_has_questions():
            self.get_next_question()
        else:
            self.score_label.config(text=f"You've completed the quiz.",
                                    font=("Arial", 15, "italic"))
            self.score_label.grid(row=0, column=0, columnspan=2)
            self.canvas.itemconfig(self.question_text, text=f"Your final score was: "
                                                            f"{self.quiz.score}/{self.quiz.question_number} 🤯",
                                   font=("Arial", 15, "bold"))

    def get_feedback(self, answer):
        """
        Provides visual feedback based on the correctness of the user's answer.

        Args:
        - answer (bool): True if the answer was correct, False otherwise.
        """
        if answer:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(500, self.still_has_questions)

    def check_true(self):
        """Callback function for the 'True' button."""
        ans = self.quiz.check_answer("True")
        self.get_feedback(ans)

    def check_false(self):
        """Callback function for the 'False' button."""
        ans = self.quiz.check_answer("False")
        self.get_feedback(ans)

