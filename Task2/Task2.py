import tkinter as tk
import random
import os

root = tk.Tk()
root.title("Alexa tell me a Joke")
root.geometry("600x400")

# Global Variables 
Current_Joke = None 
Show_Punchline = False

# Finds the txt file in the current folder
Current_Folder = os.path.dirname(os.path.abspath(__file__))
File_Path_Jokes = os.path.join(Current_Folder, "randomJokes.txt")

# Main function that loads the joke
def Jokes():
    global Current_Joke, Show_Punchline

    # Shows the punchline if ready
    if Show_Punchline and Current_Joke:
        Question, Punchline = Current_Joke
        Joke.config(text=f"{Question}\n\n{Punchline}")
        Tell_me.config(text="Tell me another Joke", command=Jokes)
        Show_Punchline = False
        return

    # Stores the jokes from the file
    jokes = []
    # Reads the jokes in the file and separates them into 2 lines
    try:
        with open(File_Path_Jokes, "r") as file:
            for line in file:
                if "?" in line:
                    parts = line.strip().split("?", 1)
                    if len(parts) == 2:
                        Question, Punchline = parts
                        jokes.append((Question.strip() + "?", Punchline.strip()))
    # Shows if the file can't be found
    except FileNotFoundError:
        Joke.config(text=f"Can't find: \n{File_Path_Jokes}")
        return

    # Picks a random joke
    if jokes:
        Current_Joke = random.choice(jokes)
        Question, _ = Current_Joke
        Joke.config(text=Question)
        Tell_me.config(text="Reveal Punchline", command=Jokes)
        Show_Punchline = True
    # Shows if there are no jokes in the file
    else:
        Joke.config(text="No jokes found in file.")

# Function to start the joke and punchline
def start_jokes():
    # Removes the Welcome screen
    Alexa.destroy()
    Start.destroy()

    # Show joke and buttons
    Joke.place(relx=0.5, rely=0.4, anchor="center")
    Tell_me.place(relx=0.5, rely=0.75, anchor="center")

    # Starts the first joke
    Jokes()

# Welcome
Alexa = tk.Label(root, text="Welcome to\nAlexa, Tell me a Joke!", font=("Times New Roman", 32, "bold"), justify="center")
Alexa.place(relx=0.5, rely=0.4, anchor="center")

# Button to start the app
Start = tk.Button(root, text="Tell me a Joke", font=("Times New Roman", 20, "bold"), command=start_jokes)
Start.place(relx=0.5, rely=0.75, anchor="center")

# Label for showing the jokes
Joke = tk.Label(root, text="", font=("Times New Roman", 24), wraplength=550, justify="center")

# Button to either reveal punchline or load the next joke
Tell_me = tk.Button(root, text="Tell me a Joke", font=("Times New Roman", 24, "bold"), command=Jokes)

root.mainloop()