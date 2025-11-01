import tkinter as tk
from tkinter import ttk
from tkinter import messagebox 
from tkinter import simpledialog
import os

# Finds the txt file in the current folder
Current_Folder = os.path.dirname(os.path.abspath(__file__))
File_Path_Students = os.path.join(Current_Folder, "studentMarks.txt")

# Class that holds the information of the students
class Student:
    def __init__(self, student_number, name, coursework_marks, exam_mark):
        self.student_number = student_number
        self.name = name
        self.coursework_marks = coursework_marks
        self.exam_mark = exam_mark

    # Function that takes the sum total of the coursework
    def total_coursework(self):
        return sum(self.coursework_marks)

    # Function that takes the sum of both courseworks and exam
    def total_marks(self):
        return self.total_coursework() + self.exam_mark

    # Function that gets the percentage of the total marks
    def percentage(self):
        return (self.total_marks() / 160) * 100

    # Function that determines the grade of the student based on percentage
    def grade(self):
        p = self.percentage()
        if p >= 70:
            return "A"
        elif p >= 60:
            return "B"
        elif p >= 50:
            return "C"
        elif p >= 40:
            return "D"
        else:
            return "F"

    # Function that returns a full summary of the student
    def display_full(self):
        return (f"Name: {self.name}\n"
                f"Student Number: {self.student_number}\n"
                f"Total Coursework: {self.total_coursework()}\n"
                f"Exam Mark: {self.exam_mark}\n"
                f"Overall Percentage: {self.percentage():.2f}%\n"
                f"Grade: {self.grade()}")

# Function that loads all the students data from the txt file
def load_student_data(file_path):

    # Stores the data of the students from the file
    students = []
    
    # Reads the contents of the file and splits it into 6 parts
    try:
        with open(file_path, "r") as file:
            file.readline()
            for line in file:
                parts = line.strip().split(",")
                if len(parts) >= 6:
                    students.append(Student(
                        int(parts[0]), parts[1], list(map(int, parts[2:5])), int(parts[5])
                    ))

    # Shows if the file can't be found
    except FileNotFoundError:
        messagebox.showerror(f"Can't Find: {file_path}")
    return students

# Function that saves the student data to the txt file
def save_data_student(file_path, students):

    # Writes the file with contents based on the given criteria
    with open(file_path, "w") as file:
        file.write(f"{len(students)}\n")
        for s in students:
            file.write(f"{s.student_number},{s.name},{s.coursework_marks[0]},"
                       f"{s.coursework_marks[1]},{s.coursework_marks[2]},{s.exam_mark}\n")

#
# Class for the main Application
class StudentRecordApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Manager")
        self.root.geometry("1100x550")

        # Load all students from file
        self.students = load_student_data(File_Path_Students)

        # Title
        tk.Label(root, text="Student Manager", font=("Times New Roman", 24, "bold")).pack(pady=10)

        # Buttons Menu
        Button_frame = tk.Frame(root)
        Button_frame.pack(pady=10)
        buttons = [
            ("View All", self.view_all_students),
            ("View Student", self.view_individual_student),
            ("Highest Score", self.show_highest_score_student),
            ("Lowest Score", self.show_lowest_score_student),
            ("Sort Records", self.sort_student_records),
            ("Add Student", self.add_student_record),
            ("Delete Student", self.delete_student_record),
            ("Update Student", self.update_student_record),
        ]

        # Placement for the buttons
        for i, (text, cmd) in enumerate(buttons):
            tk.Button(Button_frame, text=text, width=18, font=("Times New Roman", 12), command=cmd)\
                .grid(row=i//4, column=i%4, padx=15, pady=10)

        # Frame for the text
        self.Text_frame = tk.Frame(root)
        self.Text_frame.pack(fill="both", expand=True, padx=10, pady=10)

        # Text where all the information will be
        self.Text = tk.Text(self.Text_frame, font=("Courier", 12), wrap="none")
        self.Text.pack(fill="both", expand=True, side="left")

        # Scrollbar for vertical scrolling
        y_scroll = tk.Scrollbar(self.Text_frame, orient="vertical", command=self.Text.yview)
        y_scroll.pack(side="right", fill="y")
        self.Text.config(yscrollcommand=y_scroll.set)

        # Message for the user and disables editing
        self.Text.insert("1.0", "Select an action to display information here...")
        self.Text.config(state="disabled")

    # Function that clears and shows information on the frame
    def Prompt(self, content):
        self.Text.config(state="normal")
        self.Text.delete("1.0", "end")
        self.Text.insert("1.0", content)
        self.Text.config(state="disabled")

    # Function that formats the table to show student's data
    def table(self, students_list):
        header = "{:<8} {:<25} {:<8} {:<6} {:<8} {:<10} {:<6}\n".format(
            "Number", "Name", "Course", "Exam", "Total", "Percent", "Grade"
        )
        header += "-"*80 + "\n"
        body = ""
        for s in students_list:
            body += "{:<8} {:<25} {:<8} {:<6} {:<8} {:<10.1f} {:<6}\n".format(
                s.student_number, s.name, s.total_coursework(), s.exam_mark,
                s.total_marks(), s.percentage(), s.grade()
            )
        return header + body

    # Function that displays all the students with the formatted table
    def view_all_students(self):
        if not self.students:
            self.Prompt("No students available.")
            return
        Table_text = self.table(self.students)
        Average = sum(s.percentage() for s in self.students)/len(self.students)
        Table_text += f"\nTotal Students: {len(self.students)} | Average: {Average:.2f}%"
        self.Prompt(Table_text)

    # Function that allows to view a student based on name or student number
    def view_individual_student(self):
        if not self.students:
            self.Prompt("No students available.")
            return
        Dialog = simpledialog.askstring("Search", "Enter student name or number:")
        if not Dialog:
            return
        Checker = [s for s in self.students if Dialog.lower() in s.name.lower() or Dialog==str(s.student_number)]
        if not Checker:
            self.Prompt("Student not found.")
            return
        self.Prompt(Checker[0].display_full())

    # Function that shows the student with the highest total marks
    def show_highest_score_student(self):
        if not self.students:
            self.Prompt("No students available.")
            return
        Highest = max(self.students, key=lambda s: s.total_marks())
        self.Prompt(Highest.display_full())

    # Function that shows the student with the lowest total marks
    def show_lowest_score_student(self):
        if not self.students:
            self.Prompt("No students available.")
            return
        Lowest = min(self.students, key=lambda s: s.total_marks())
        self.Prompt(Lowest.display_full())

    # Function that sorts all student records by total marks
    def sort_student_records(self):
        if not self.students:
            self.Prompt("No students available.")
            return
        Sorting = messagebox.askquestion("Sorter", "Ascending to show Highest first = Yes Descending to Show Lowest first = No")
        Reverse = Sorting == "yes"
        List_Sorted = sorted(self.students, key=lambda s: s.total_marks(), reverse=Reverse)
        Table_text = self.table(List_Sorted)
        self.Prompt(Table_text)

    # Function that allows to add a new student in the file
    def add_student_record(self):
        try:
            Student_Number = int(simpledialog.askstring("Add", "Student number (1000-9999):"))
            Student_Name = simpledialog.askstring("Add", "Student name:")
            Course_1 = int(simpledialog.askstring("Add", "Coursework 1 (0-20):"))
            Course_2 = int(simpledialog.askstring("Add", "Coursework 2 (0-20):"))
            Course_3 = int(simpledialog.askstring("Add", "Coursework 3 (0-20):"))
            Exam = int(simpledialog.askstring("Add", "Exam Mark (0-100):"))
            self.students.append(Student(Student_Number, Student_Name, [Course_1, Course_2, Course_3], Exam))
            save_data_student(File_Path_Students, self.students)
            self.Prompt(f"Student {Student_Name} added successfully!")
        except:
            self.Prompt("Invalid input. Student not added.")

    # Function that allows to delete a student in the file
    def delete_student_record(self):
        Dialog = simpledialog.askstring("Delete", "Enter name or number:")
        if not Dialog:
            return
        Checker = [s for s in self.students if Dialog.lower() in s.name.lower() or Dialog==str(s.student_number)]
        if not Checker:
            self.Prompt("Student not found.")
            return
        Student = Checker[0]
        if messagebox.askyesno("Confirm Delete", f"Delete {Student.name}?"):
            self.students.remove(Student)
            save_data_student(File_Path_Students, self.students)
            self.Prompt(f"Student {Student.name} deleted successfully.")

    # Function that allows to update an student's data in the file
    def update_student_record(self):
        Dialog = simpledialog.askstring("Update", "Enter name or number:")
        if not Dialog:
            return
        Checker = [s for s in self.students if Dialog.lower() in s.name.lower() or Dialog==str(s.student_number)]
        if not Checker:
            self.Prompt("Student not found.")
            return
        Student = Checker[0]
        Menu = simpledialog.askstring("Update Menu", "1-Name\n2-Coursework\n3-Exam")
        if Menu == "1":
            Student_New_Name = simpledialog.askstring("New Name", "Enter new name:")
            if Student_New_Name:
                Student.name = Student_New_Name
        elif Menu == "2":
            try:
                Course_1 = int(simpledialog.askstring("Coursework", "New Mark 1:"))
                Course_2 = int(simpledialog.askstring("Coursework", "New Mark 2:"))
                Course_3 = int(simpledialog.askstring("Coursework", "New Mark 3:"))
                Student.coursework_marks = [Course_1, Course_2, Course_3]
            except:
                self.Prompt("Invalid coursework marks.")
                return
        elif Menu == "3":
            try:
                Student.exam_mark = int(simpledialog.askstring("Exam", "New exam mark:"))
            except:
                self.Prompt("Invalid exam mark.")
                return
        else:
            self.Prompt("No changes made.")
            return
        save_data_student(File_Path_Students, self.students)
        self.Prompt(f"Student {Student.name} updated successfully.")

root = tk.Tk()
app = StudentRecordApp(root)
root.mainloop()