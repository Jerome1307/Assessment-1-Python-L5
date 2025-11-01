# Assessment 1 - Advanced Programming (Python)

## Brief Overview
Our assessment was to complete 3 exercises using a combination of **Python** and **Tkinter** this allows us the create and complete the task with GUI. 

The assessment tests our knowledge and capabilities of Python and Tkinter techniques.

Learning Websites like **Sololearn** and **Cisco** help expand our knowledge to be able to complete these exercises

The following are the Exercises that we need to complete to complete this assessment:<br>
**Exercise 1 - Maths Quiz** <br>
**Exercise 2 - Alexa Tell me a Joke** <br>
**Exercise 3 - Student Manager** <br>

## Exercise 1 - Maths Quiz
We are tasked to make a Math quiz with the following difficulties:

<pre>
    1.Easy              range (0 - 9)
    2.Moderate          range (10 - 99)
    3.Hard              range (1000 - 9999)
</pre>

After selecting the difficulty it randomizes the two numbers based on the difficulty and also picks either addition or subtraction randomly

Then it allows the user to enter a number for an answer if the user gets it correct they get +10 if they get it wrong the first time you get a second attempt which only gives +5 and if wrong the second time then it moves to the next question while revealing the correct answer

The following functions where also needed to complete the Exercise/Task:

    ● displayMenu: A function that displays the difficulty level menu at the beginning of the quiz.

    ● randomInt: A function that determines the values used in each question. The min and max values of the numbers should be based on the difficulty level chosen as described above.

    ● decideOperation: A function that randomly decides whether the problem is an addition or subtraction problem and returns a char.

    ● displayProblem: A function that displays the question to the user and accepts their answer.

    ● isCorrect: A function that checks whether the users answer was correct and outputs an appropriate message

    ● displayResults: function that outputs the users final score out of a possible 100 and ranks the user based on their score (e.g. A+ for a score over 90)

After the quiz it gives them a grade based on their score and asks them if they want to play again

## Exercise 2 - Alexa Tell me a Joke
We are tasked to make an app that is similar to asking Alexa to tell the user a joke

A provided file of **randomJokes.txt** is given which has the setup and punchline

We must make it so that when the user clicks Alexa Tell me a Joke it should show first the setup and then allow the user to reveal the punchline

Afterwards it should allow the user to request for another joke until they decide to quit the app

## Exercise 3 - Student Manager 

We are tasked to make an app that manages the Student Records

A provided file of **studentMarks.txt** is given which has the following

<pre>
    1.Student Number
    2.Student Name
    3.Coursemark 1
    4.Coursemark 2
    5.Coursemark 3
    6.Exam
</pre>

The following is what is needed to complete this Exercise/Task:

## View all student records

Allows the user to view all the student's data/record with all data provided in the file being 

    ●Students Name

    ●Students Number

    ●Total coursework mark

    ●Exam Mark

    ●Overall percentage (coursework and examination marks contributing in direct proportion to the marks available i.e. the percentage is based on the potential total of 160 marks).

    ●Student grade ( ‘A’ for 70%+, ‘B’ for 60%-69%, ‘C’ for 50%-59%, ‘D’ for 40%-49%, ‘F’ for under 40% )

After showing all the students it also takes the total number of students as well as the average percentage of all

## View individual student record

Allows the user to view a specific student based on either their name or student number

## Show student with highest overall mark

Allows the user to view the student with the highest mark

## Show student with lowest overall mark

Allows the user to view the student with the lowest mark

## Extension Problem

An additional challenge for this Exercise

## Sort student records

Allows the user to sort the students record/data by ascending or descending order

## Add a student record

Allows the user to add a student with all required data/information

## Delete a student's record

Allows the user to select a student by either their name or student number and delete them from the record from the file

## Update a student's record

Allows the user to select a student by either their name or student number and update a specific data from the file
