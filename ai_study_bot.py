import tkinter as tk
from tkinter import messagebox
import random


# ---------------- AI LOGIC ----------------

def generate_response(question):
    question = question.lower()

    responses = {
        "python": """
Python is a high-level programming language known for
its simple syntax.

Important concepts:
• Variables
• Conditions
• Loops
• Functions
• OOP
• File Handling
• Libraries
""",

        "oops": """
OOP means Object-Oriented Programming.

Four major concepts:

1. Encapsulation
2. Inheritance
3. Polymorphism
4. Abstraction
""",

        "database": """
A database stores and organizes information.

Important DBMS concepts:

• Tables
• Primary Keys
• Foreign Keys
• SQL
• Normalization
• Transactions
• Indexing
""",

        "blockchain": """
Blockchain is a distributed ledger technology.

Main concepts:

• Blocks
• Hashing
• Distributed network
• Consensus
• Smart contracts
• Cryptocurrencies
"""
    }

    for topic, answer in responses.items():
        if topic in question:
            return answer

    return """
I don't have a specific answer for that topic yet.

Try asking about:

• Python
• OOP
• Database
• Blockchain

You can also use the Quiz and Study Plan features.
"""


def ask_question():
    question = question_entry.get()

    if not question.strip():
        return

    answer = generate_response(question)

    chat.insert(tk.END, f"\nYou: {question}\n")
    chat.insert(tk.END, f"Study Buddy: {answer}\n")

    question_entry.delete(0, tk.END)


# ---------------- QUIZ ----------------

quiz_questions = [
    ("Which keyword defines a function in Python?", 
     ["func", "def", "function", "define"], "def"),

    ("Which data structure stores key-value pairs?",
     ["List", "Tuple", "Dictionary", "Set"], "Dictionary"),

    ("Which language is mainly used for styling web pages?",
     ["Python", "CSS", "SQL", "C++"], "CSS"),

    ("What does OOP stand for?",
     ["Object Oriented Programming",
      "Open Online Program",
      "Object Operating Protocol",
      "None"], 
     "Object Oriented Programming")
]


def start_quiz():
    question, options, answer = random.choice(quiz_questions)

    quiz_window = tk.Toplevel(root)
    quiz_window.title("Study Quiz")
    quiz_window.geometry("500x350")

    tk.Label(
        quiz_window,
        text=question,
        font=("Arial", 15, "bold"),
        wraplength=450
    ).pack(pady=30)

    for option in options:

        def check_answer(selected=option):
            if selected == answer:
                messagebox.showinfo("Result", "🎉 Correct!")
            else:
                messagebox.showerror(
                    "Result",
                    f"❌ Wrong!\nCorrect answer: {answer}"
                )

        tk.Button(
            quiz_window,
            text=option,
            width=30,
            command=check_answer
        ).pack(pady=5)


# ---------------- STUDY PLAN ----------------

def study_plan():
    plan = """
📚 TODAY'S STUDY PLAN

09:00 - 10:00
Python Programming

10:15 - 11:15
Data Structures

11:30 - 12:30
Database Management

14:00 - 15:00
Project Development

16:00 - 16:30
Revision

20:00 - 20:30
Practice Quiz
"""

    messagebox.showinfo("Study Plan", plan)


# ---------------- GUI ----------------

root = tk.Tk()
root.title("🤖 AI Study Buddy")
root.geometry("700x650")

tk.Label(
    root,
    text="🤖 AI Study Buddy",
    font=("Arial", 24, "bold")
).pack(pady=15)

chat = tk.Text(
    root,
    height=25,
    width=80,
    wrap=tk.WORD
)

chat.pack(padx=15, pady=10)

question_entry = tk.Entry(
    root,
    width=60
)

question_entry.pack(side=tk.LEFT, padx=15)

tk.Button(
    root,
    text="Ask",
    command=ask_question
).pack(side=tk.LEFT)

button_frame = tk.Frame(root)
button_frame.pack(pady=20)

tk.Button(
    button_frame,
    text="📝 Take Quiz",
    command=start_quiz
).pack(side=tk.LEFT, padx=10)

tk.Button(
    button_frame,
    text="📚 Study Plan",
    command=study_plan
).pack(side=tk.LEFT, padx=10)

root.mainloop()