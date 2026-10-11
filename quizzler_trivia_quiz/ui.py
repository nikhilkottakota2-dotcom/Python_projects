from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self,quiz_brain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20,pady=20,bg=THEME_COLOR)
        self.score_label=Label(text="Score:0",fg="white",bg=THEME_COLOR)
        self.score_label.grid(row=0,column=1)
        self.canvas = Canvas(width=300,height=250,bg="white")
        self.question_text = self.canvas.create_text(150,125,width=280,text="some quesions",fill = THEME_COLOR,font=("Arial",20,"italic"))
        self.canvas.grid(row=1,column=0,columnspan=2,pady=50)
        self.true_image = PhotoImage(file=r"C:\python\100_days_bootcamp\quizzler_trivia_quiz\images\true.PNG")
        self.true_button = Button(image=self.true_image,highlightthickness=0,command=self.true_passed)
        self.true_button.grid(row=2,column=0)
        self.false_image = PhotoImage(file=r"C:\python\100_days_bootcamp\quizzler_trivia_quiz\images\false.PNG")
        self.false_button = Button(image=self.false_image,highlightthickness=0,command=self.false_passed)
        self.false_button.grid(row=2,column=1)

        self.next_question()
        self.window.mainloop()

    def next_question(self):
        self.canvas.config(bg="white")
        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.question_text,text=q_text) 

    def true_passed(self):
        self.give_feedback(self.quiz.check_answer("True"))
    def false_passed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)
    def give_feedback(self,is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.score_label.config(text=f"Score: {self.quiz.score}")
        self.window.after(1000, self.next_question)