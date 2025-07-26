import tkinter as tk
from tkinter import messagebox

# Questions for Table of 5
questions = [
    (2, 5),
    (4, 5),
    (6, 5),
    (10, 5)
]

rewards = [
    "Mittens gets a warm cookie! 🍪",
    "Mittens finds a chocolate chip cookie! 🍪",
    "The leaf floats away, and Mittens gets another cookie! 🍪",
    "Mittens enters the Cookie Castle and finds a Giant Cookie Cake! 🎂🍪"
]

class CookieQuestGame:
    def __init__(self, root):
        self.root = root
        self.root.title("🍪 Cookie Quest – Help the Cat!")
        self.root.geometry("450x300")
        self.root.configure(bg="#FFF8E1")

        self.question_index = 0

        self.title_label = tk.Label(root, text="🐱 Cookie Quest – Help Mittens!", font=("Arial", 16, "bold"), bg="#FFF8E1")
        self.title_label.pack(pady=10)

        self.story_label = tk.Label(root, text="", font=("Arial", 12), bg="#FFF8E1")
        self.story_label.pack(pady=10)

        self.question_label = tk.Label(root, text="", font=("Arial", 14), bg="#FFF8E1")
        self.question_label.pack()

        self.answer_entry = tk.Entry(root, font=("Arial", 14), justify='center')
        self.answer_entry.pack(pady=10)

        self.submit_btn = tk.Button(root, text="Submit Answer", font=("Arial", 12), command=self.check_answer, bg="#FFD54F")
        self.submit_btn.pack(pady=10)

        self.feedback_label = tk.Label(root, text="", font=("Arial", 12), fg="green", bg="#FFF8E1")
        self.feedback_label.pack()

        self.next_question()

    def next_question(self):
        if self.question_index < len(questions):
            num1, num2 = questions[self.question_index]
            self.story_label.config(text=f"🚪 Door {self.question_index + 1}")
            self.question_label.config(text=f"What is {num1} x {num2}?")
            self.answer_entry.delete(0, tk.END)
            self.feedback_label.config(text="")
        else:
            self.finish_game()

    def check_answer(self):
        user_input = self.answer_entry.get()
        try:
            user_answer = int(user_input)
            num1, num2 = questions[self.question_index]
            correct_answer = num1 * num2

            if user_answer == correct_answer:
                self.feedback_label.config(text=f"✅ Correct! {rewards[self.question_index]}", fg="green")
                self.question_index += 1
                self.root.after(1500, self.next_question)
            else:
                self.feedback_label.config(text="❌ Oops! Try again!", fg="red")
        except ValueError:
            self.feedback_label.config(text="⚠️ Please enter a number!", fg="orange")

    def finish_game(self):
        messagebox.showinfo("🎉 You Did It!", "Tarak helped Mittens collect all the cookies!\nYou are awesome! 🐾")
        self.root.destroy()

# Create GUI Window
root = tk.Tk()
game = CookieQuestGame(root)
root.mainloop()
