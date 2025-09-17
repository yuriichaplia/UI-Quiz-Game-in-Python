import tkinter
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = tkinter.Tk()
        self.window.title("Quizzler")
        self.window.config(background=THEME_COLOR, padx = 20, pady = 20)

        self.score = tkinter.Label(text="Score:0", highlightthickness = 0, fg="white", bg=THEME_COLOR)
        self.score.grid(row = 0, column = 1)

        self.canvas = tkinter.Canvas(width = 300, height = 250, background="white")
        self.text = self.canvas.create_text(150, 125,
                                            width = 280,
                                            text="Some Question Text",
                                            fill=THEME_COLOR,
                                            font=("Arial", 20, "italic"))
        self.canvas.grid(row = 1, column = 0, columnspan = 2, pady = 50)

        image_1 = tkinter.PhotoImage(file="images/true.png")
        self.green_button = tkinter.Button(image=image_1, highlightthickness=0, command = self.green_answer)
        self.green_button.grid(row = 2, column = 0)

        image_2 = tkinter.PhotoImage(file="images/false.png")
        self.red_button = tkinter.Button(image=image_2, highlightthickness=0, command = self.red_answer)
        self.red_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(background="white")
        if self.quiz.still_has_questions():
            self.score.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.text, text=q_text)
        else:
            self.canvas.itemconfig(self.text, text="You have reached the end of the quiz")
            self.green_button.config(state="disabled")
            self.red_button.config(state="disabled")

    def green_answer(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def red_answer(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_true):
        if is_true:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        self.window.after(1000, self.get_next_question)