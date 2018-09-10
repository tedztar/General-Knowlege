#all print statements are for testing and do not have any effect on the game

import tkinter as tk                # python 3
from tkinter import font  as tkfont # python 3
import os
from random import random

#iniseised the program
main = tk.Tk()
main.geometry("500x300")
main.title("the title goes here")

#Set the frams that will be used
welcome = tk.Frame(main)
start = tk.Frame(main)
stats = tk.Frame(main)
game = tk.Frame(main)
answer = tk.Frame(main)


for frame in (welcome, start, stats, game, answer):
    frame.grid(row=1, column=1, sticky="nesw")

def display(frame):
    frame.tkraise()

#Inisiate variables
Questions = ["What’s the medical term for low blood sugar?", "What’s the common term for a cerebrovascular accident?", "What star other than the sun is closest to the earth?", "What is the most widely eaten fish in the world?"]
Answers = ["Hypoglycemia", "Stroke", "Proxima Centauri", "The Herring"]
AnsweredQuestions = []
UserName = ""
NumOfQuestions = len(Questions)
userName = tk.StringVar()
Question = int()


#checks to see if the usere has been back
#and opens the save file
def namecheck():
    NumberOfAnswered = 0
    UserName = userName.get()
    FileName= UserName + ".txt"
    if os.path.exists(FileName):
        SaveFile = open(FileName,  "r+")
        AnsweredQuestions = SaveFile.readlines()
        for i in AnsweredQuestions:
            if i == "1\n":
                NumberOfAnswered += 1
        WelcomeBack.configure(text="Welcome back " + UserName + ".\nYou have answered "+ str(NumberOfAnswered) +" questions.") #sets the text for the welcome back screen
        display(stats)
    else:
        SaveFile = open(FileName,  "a+")
        i=0
        #SaveFile.close()
        #SaveFile = open(FileName, "r+")
        while i < NumOfQuestions:
            SaveFile.write("0")
            SaveFile.write("\n")
            i += 1
        AnsweredQuestions = SaveFile.readlines()
        WelcomeText.configure(text="Welcome " + UserName + ".\nPush the button below to start.") #sets the text for the welcome screen
        display(start)

#gets the next question for the user
def questionget():
    i = int(random(0, NumOfQuestions+1))
    FoundQuestion = False
    while FoundQuestion == False:
        if AnsweredQuestions(i) == 0:
            question = i
            FoundQuestion = True
        else:
            i =+ 1

    QuestionText.configure(WelcomeText=Questions[Question])
    display(game)
    print("questionget")
  
#checks the answer the user put in
def questioncheck():
    userAnswer=UserAnswer.get()
    userAnswer.lower()
    correctAnswer=Answers(Question)
    correctAnswer.lower
    if userAnswer == correctAnswer:
        Correct.configure(text="That is correct./nYou guessed:")
        CorrectAnswer.congidure(text=correctAnswer)
        AnsweredQuestions[Question]="1\n"
        display(answer)
        print("correct") #for testing
    else:
        Correct.configure(text="That is incorrect./nThe correct answer is:")
        CorrectAnswer.configure(text=correctAnswer)
        display(answer)
        print("incorrect") #for testing
    print("questioncheck")   #for testing

#program start screen
welcomeText = tk.Label(welcome, text="Welcome to the General Knowlege quiz.\nWhat is your name?",font=("Helvetica",15)).pack(padx=60,pady=100)
submit = tk.Button(welcome, text="Submit", command= lambda: namecheck()).pack(side="right")
NameEntery = tk.Entry(welcome, textvariable = userName, width = 50 ).pack(pady=10)


#returning user stats screen
WelcomeBack = tk.Label(stats,font=("Helvetica",15))
WelcomeBack.pack()
button = tk.Button(stats, text="Continue", command=lambda: display(welcome)).pack()


#New user Start Screen
WelcomeText = tk.Label(start, text="This is page 2")
WelcomeText.pack(side="top", fill="x", pady=10)
button = tk.Button(start, text="Start",command=lambda: display(welcome)).pack()


#main game screen
QuestionText = tk.Label(game, text="This is the main game screen")
QuestionText.pack(side="top", fill="x", pady=10)
UserAnswer = tk.Entry(welcome, textvariable = userName, width = 50 ).pack(pady=10)


#answer screen
Correct = tk.Label(answer, text="This is the Answer screen")
Correct.pack(side="top", fill="x", pady=10)
CorrectAnswer = tk.Label(answer, text="This is the Answer screen")
CorrectAnswer.pack(side="top", fill="x", pady=10)



display(welcome)
main.mainloop()