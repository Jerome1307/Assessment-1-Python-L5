import tkinter as tk
import random

root = tk.Tk()
root.geometry("420x360")
root.title("Maths Quiz")

# Global Variables
Score = 0
Difficulty = 0
Question_Number = 0
Correct_Answer = 0
Attempts = 2
Lock = False

# Function that displays the title and different difficulties
def displayMenu():
    Title.place(relx=0.5, rely=0.2, anchor="center")
    Easy.place(relx=0.5, rely=0.4, anchor="center")
    Moderate.place(relx=0.5, rely=0.6, anchor="center")
    Advanced.place(relx=0.5, rely=0.8, anchor="center")

# Function that selects difficulty and Starts the quiz
def setDifficulty(level):
    global Difficulty, Question_Number, Score
    Difficulty = level
    Question_Number = 0
    Score = 0
    Title.place_forget()
    Easy.place_forget()
    Moderate.place_forget()
    Advanced.place_forget()
    Quiz_frame.place(relx=0.5, rely=0.5, anchor="center")
    nextQuestion()

# Function that randomly chooses the two numbers based on the difficulty
def randomInt():
    # Easy Difficulty
    if Difficulty == 1:
        return random.randint(0, 9)
    # Moderate Difficulty
    elif Difficulty == 2:
        return random.randint(10, 99)
    # Hard Difficulty
    else:
        return random.randint(1000, 9999)

# Function that randomly chooses if it is either addition or subtraction
def decideOperation():
    return random.choice(["+", "-"])

# Function that shows the equation and input for the answer
def displayProblem(num1, num2, op):
    """Show problem and prepare entry for answer"""
    global Correct_Answer, Attempts, Lock
    Correct_Answer = num1 + num2 if op == "+" else num1 - num2
    Attempts = 2
    Lock = False
    Answer.config(state="normal")
    Answer.delete(0, tk.END)
    Answer.focus()
    Prompt.config(text="")
    Question.config(text=f"Question {Question_Number + 1}/10")
    Equation.config(text=f"{num1} {op} {num2} =")

# Function that checks if the answer is correct or incorrect
def isCorrect(event=None):
    global Score, Question_Number, Attempts, Lock

    # This prevents repeated key presses
    if Lock:
        return

    # Checks if the answer is a nnumber
    try:
        User_Answer = int(Answer.get())

    # If it is not a number 
    except ValueError:
        Prompt.config(text="Please enter a valid number.")
        return

    # Checks if the Answer is Correct and awards the points based on attempts
    if User_Answer == Correct_Answer:
        gained = 10 if Attempts == 2 else 5  
        Score += gained
        Prompt.config(text=f"Correct! +{gained} points")
        Question_Number += 1
        Lock = True
        Answer.config(state="disabled")
        root.after(600, nextQuestion)

    # Tells user if the answer is wrong and if all attempts is used reveals the Correct Answer
    else:
        if Attempts == 2:
            Prompt.config(text="Wrong! Try once more")
            Attempts = 1
            Answer.delete(0, tk.END)
            Answer.focus()
        else:
            Prompt.config(text=f"Wrong again! The correct answer was {Correct_Answer}")
            Question_Number += 1
            Lock = True
            Answer.config(state="disabled")
            root.after(600, nextQuestion)

# Function that generates the next question or show the result
def nextQuestion():
    if Question_Number < 10:
        num1 = randomInt()
        num2 = randomInt()
        op = decideOperation()
        displayProblem(num1, num2, op)
    else:
        displayResults()

# Function that shows the score and the grade corresponding to it
def displayResults():
    Quiz_frame.place_forget()
    grade = ""
    if Score >= 90:
        grade = "A+"
    elif Score >= 80:
        grade = "A"
    elif Score >= 70:
        grade = "B"
    elif Score >= 60:
        grade = "C"
    else:
        grade = "F"
    Result.config(text=f"Your Score: {Score}/100\nGrade: {grade}")
    Result_frame.place(relx=0.5, rely=0.5, anchor="center")

# Function that returns back to the Menu screen
def playAgain():
    Result_frame.place_forget()
    displayMenu()

# Title
Title = tk.Label(root, text="Math Quiz", font=("Times New Roman", 24, "bold"))
Title.place(relx=0.5, rely=0.2, anchor="center")

# Difficulties
Easy = tk.Button(root, text="Easy", font=("Times New Roman", 16), width=12, command=lambda: setDifficulty(1))
Easy.place(relx=0.5, rely=0.4, anchor="center")

Moderate = tk.Button(root, text="Moderate", font=("Times New Roman", 16), width=12, command=lambda: setDifficulty(2))
Moderate.place(relx=0.5, rely=0.6, anchor="center")

Advanced = tk.Button(root, text="Advanced", font=("Times New Roman", 16), width=12, command=lambda: setDifficulty(3))
Advanced.place(relx=0.5, rely=0.8, anchor="center")

# Quiz frame
Quiz_frame = tk.Frame(root, width=400, height=250)

Question = tk.Label(Quiz_frame, text="", font=("Times New Roman", 16))
Question.place(relx=0.5, rely=0.1, anchor="center")

Equation = tk.Label(Quiz_frame, text="", font=("Times New Roman", 32))
Equation.place(relx=0.5, rely=0.35, anchor="center")

Answer = tk.Entry(Quiz_frame, font=("Times New Roman", 16), justify="center")
Answer.place(relx=0.5, rely=0.55, anchor="center", width=120, height=35)
Answer.bind("<Return>", isCorrect)

Prompt = tk.Label(Quiz_frame, text="", font=("Times New Roman", 16))
Prompt.place(relx=0.5, rely=0.75, anchor="center")

# Result frame
Result_frame = tk.Frame(root)

Result = tk.Label(Result_frame, text="", font=("Times New Roman", 24))
Result.pack(pady=10)

Play_Again = tk.Button(Result_frame, text="Play Again", font=("Times New Roman", 16), command=playAgain)
Play_Again.pack(pady=5)

# Start main loop
root.mainloop()
