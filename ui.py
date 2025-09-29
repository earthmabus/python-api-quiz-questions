import tkinter
from tkinter import messagebox

from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
ANSWER_FEEDBACK_SLEEP_IN_MS = 1000

class UI:
    def __init__(self, quiz : QuizBrain):
        self.m_quiz = quiz

        self.m_window = tkinter.Tk()
        self.m_window.title("Quizzler")
        self.m_window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.m_score_label = tkinter.Label(text="", fg="white", bg=THEME_COLOR)
        self.m_score_label.grid(row=0, column=1)
        self.display_score()

        self.m_canvas = tkinter.Canvas(width=300, height=250, bg="white")
        self.m_question_text = self.m_canvas.create_text(150, 125, width=280, text="[QUESTION HERE]", fill=THEME_COLOR, font=("Arial", 20, "italic"))
        self.m_canvas.grid(row=1, column=0, columnspan=2, pady=50)

        true_img = tkinter.PhotoImage(file="./images/true.png")
        #self.m_true_button = tkinter.Button(image=true_img, text="True", highlightthickness=0, command=self.true_button_clicked)
        self.m_true_button = tkinter.Button(text="True", highlightthickness=0, command=self.true_button_clicked)
        self.m_true_button.grid(row=2, column=0)

        false_img = tkinter.PhotoImage(file="./images/false.png")
        #self.m_false_button = tkinter.Button(image=false_img, text="False", highlightthickness=0, command=self.false_button_clicked)
        self.m_false_button = tkinter.Button(text="False", highlightthickness=0, command=self.false_button_clicked)
        self.m_false_button.grid(row=2, column=1)

    def next_question(self):
        current_question = self.m_quiz.next_question()
        self.m_canvas.itemconfig(self.m_question_text, text=current_question.text)

    def true_button_clicked(self):
        self.check_answer("True")

    def false_button_clicked(self):
        self.check_answer("False")

    def check_answer(self, answer):
        feedback_color = "red"
        if self.m_quiz.check_answer(answer):
            feedback_color = "green"
        self.m_canvas.config(bg=feedback_color)
        self.m_true_button.config(state=tkinter.DISABLED)
        self.m_false_button.config(state=tkinter.DISABLED)
        self.m_window.after(ANSWER_FEEDBACK_SLEEP_IN_MS, self.remove_feedback_color)

    def display_score(self):
        self.m_score_label.config(text=f"Score: {self.m_quiz.score} / {self.m_quiz.question_number}")

    def remove_feedback_color(self):
        self.m_canvas.config(bg="white")

        self.m_true_button.config(state=tkinter.NORMAL)
        self.m_false_button.config(state=tkinter.NORMAL)

        # update the score and get the next question
        self.display_score()
        if self.m_quiz.still_has_questions():
            self.next_question()
        else:
            result = messagebox.askyesno("All Done", f"That was the final question!\nYou scored {self.m_quiz.score} of {self.m_quiz.question_number}\nWould you like to play again?")
            if result:
                self.m_quiz.reset()
                self.m_quiz.load_questions_from_opentdb()

                self.display_score()

                self.next_question()
            else:
                self.m_window.quit()

    def loop(self):
        self.m_window.mainloop()