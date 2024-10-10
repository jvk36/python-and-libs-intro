from tkinter import *
from src.quizzler_brain import QuizBrain


THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text="Score: 0", font=("Arial", 12, "normal"), fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(150, 125, text="Some question text",
                                                     font=("Arial", 20, "italic"), width=280)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=20)

        true_img = PhotoImage(file="./images/quizzler-true.png")
        self.true_button = Button(image=true_img, bg=THEME_COLOR, highlightthickness=0,
                             padx=20, pady=20, command=self.true_button_clicked)
        self.true_button.grid(row=2, column=0)

        false_img = PhotoImage(file="./images/quizzler-false.png")
        self.false_button = Button(image=false_img, bg=THEME_COLOR, highlightthickness=0,
                              padx=20, pady=20, command=self.false_button_clicked)
        self.false_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def give_feedback(self, result):
        if result:
            self.canvas.config(bg="green") # , highlightthickness=0)
        else:
            self.canvas.config(bg="red") # , highlightthickness=0)
        self.window.after(1000, self.get_next_question)

    def true_button_clicked(self):
        result = self.quiz.check_answer("True")
        self.give_feedback(result)

    def false_button_clicked(self):
        result = self.quiz.check_answer("False")
        self.give_feedback(result)

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You have reached the end of the quiz.")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")
