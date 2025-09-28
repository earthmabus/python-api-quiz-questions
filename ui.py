import tkinter

THEME_COLOR = "#375362"

class UI:
    def __init__(self):
        self.m_window = tkinter.Tk()
        self.m_window.title("Quizzler")
        self.m_window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.m_score_label = tkinter.Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.m_score_label.grid(row=0, column=1)

        self.m_canvas = tkinter.Canvas(width=300, height=250, bg="white")
        self.m_question_text = self.m_canvas.create_text(150, 125, text="[QUESTION HERE]", fill=THEME_COLOR, font=("Arial", 20, "italic"))
        self.m_canvas.grid(row=1, column=0, columnspan=2, pady=50)

        true_img = tkinter.PhotoImage(file="images/true.png")
        self.m_true_button = tkinter.Button(image=true_img, highlightthickness=0, command=self.true_button_clicked)
        self.m_true_button.grid(row=2, column=0)

        false_img = tkinter.PhotoImage(file="images/false.png")
        self.m_false_button = tkinter.Button(image=false_img, highlightthickness=0, command=self.false_button_clicked)
        self.m_false_button.grid(row=2, column=1)

    def true_button_clicked(self):
        print("you clicked true")

    def false_button_clicked(self):
        print("you clicked false")

    def loop(self):
        self.m_window.mainloop()