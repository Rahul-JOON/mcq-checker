import os
import tkinter as tk
import datetime
from tkinter import *
from tkinter import ttk
import threading
from functools import partial
from data import catalog

closer = False

class Countdown(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.create_widgets()
        self.show_widgets()
        self.seconds_left = 0
        self._timer_on = False
    def show_widgets(self):
        self.label1.grid(column=1, row=1)
        self.label2.grid(column=2, row=4)
        self.entry1.grid(column=1,row=2)
        self.entry2.grid(column=2,row=5)
        self.start.grid(column=1,row=3)

    def create_widgets(self):
        self.label1 = tk.Label(self, width=10, text = '00:00:00')
        self.label2 = tk.Label(self, text='Question number')
        self.entry1 = tk.Entry(self, justify = 'center')
        self.entry2 = tk.Entry(self, justify = 'center')
        self.entry1.insert(END, '10800')
        self.entry1.focus_set()
        self.start = tk.Button(self, width=10, text = 'Start', command = self.start_button)
    def countdown(self):
        self.label1['text'] = self.convert_seconds_left_to_time()
        if self.seconds_left:
            self.seconds_left -= 1
            self._timer_on = self.after(1000, self.countdown)
        else :
            self._timer_on = False

    def start_button(self):
        self.seconds_left = int(self.entry1.get())    
        self.stop_timer()
        self.countdown()
        self.entry1.delete(0,"end")

    def stop_timer(self):
        if self._timer_on:
            self.after_cancel(self._timer_on)
            self._timer_on = False
        
    def convert_seconds_left_to_time(self):
        return datetime.timedelta(seconds=self.seconds_left)
def timer_submitter_takinganswers():
    def value_taker(value):
        global no_of_questions
        if countdown.entry2.get().isdigit():
            if not int(countdown.entry2.get()) > int(no_of_questions):
                catalog[int(countdown.entry2.get())] = value
                countdown.entry2.delete(0, 'end')
        l = list(catalog)
        l.sort()
        r = 10
        c = 0
        for s in l:
            Label(text=f'{s}:{catalog[s]}').grid(row=r, column=c)
            r += 1
            if r>25:
                c +=1
                r = 10
                
    root = tk.Tk()
    countdown = Countdown(root)
    countdown.grid(column=1, row= 2)
    abutton = Button(root, text='A', padx=5,command=partial(value_taker,'a'))
    bbutton = Button(root, text='B', padx=5,command=partial(value_taker,'b'))
    cbutton = Button(root, text='C', padx=5,command=partial(value_taker,'c'))
    dbutton = Button(root, text='D', padx=5,command=partial(value_taker,'d'))
    abutton.grid(column=1, row=6)
    bbutton.grid(column=2, row=6)
    cbutton.grid(column=1, row=7)
    dbutton.grid(column=2, row=7)
    Label(text="Answers :", padx=50,).grid(column=1, row=8)
    exitbutton = Button(root, text = 'Submit Exam!', padx= 25,command=root.destroy)
    exitbutton.grid(column=2, row=2)
    root.mainloop()



name = input("Enter your name : ")
date = input("Enter the Date : ")
exam_name = input("Enter the exam name : ")
number_for_correct_ans = int(input("Enter the number to be awarded for every correct ans. "))
no_of_questions = input('Enter the number of questions : ')
while True:
    solution_file = input("Enter the name of the solution file : ")
    solution_file = solution_file + '.txt'
    os.chdir('V:\Python\mcq checker\solution files')
    try :
        with open(f"{solution_file}", 'r') as solutions:
            content = solutions.readlines()
            answer_key = {}
            for i in range(1, int(no_of_questions) + 1):
                answer_key[i] = content[0][i - 1]
            break
    except FileNotFoundError:
        print("Wrong name of the file.")
    except IndexError:
        print("Number of questions according to user are not equal to the number of questions in answer key")

answers_by_user = {}
print('-'*90)
print("Start Now! Mark your clock for 3 hours.")
timer_submitter_takinganswers()
answers_by_user = catalog
marks = 0
correct_ans = 0
question_to_revisit = []

for j in answers_by_user:
    if answers_by_user[j] == answer_key[j]:
        marks += number_for_correct_ans
        correct_ans += 1
    else :
        marks -= 1
        question_to_revisit.append(j)

quetions_attempted = len(answers_by_user)
wrong_ans = quetions_attempted - correct_ans
questions_not_attempted = []

for k in range(1, int(no_of_questions) + 1):
    if k not in answers_by_user:
        questions_not_attempted.append(k)

record = [f'Name - {name}', f'Date - {date}', f'Exam - {exam_name}', f'Total questions = {int(no_of_questions)}', f'Marks obtained = {marks} :\/: +{number_for_correct_ans} for correct ans and -1 for wrong ans', f'correct ans = {correct_ans}', f'wrong ans = {wrong_ans}', f'Questions to revisit(questions answered wrong) = {question_to_revisit}', f'Questions not attempted = {questions_not_attempted}'] 

with open('Records.txt', 'a+') as writer:
    for g in record:
        writer.writelines(g + '\n')
    writer.write('-'*90+'\n\n')

root = tk.Tk()
root.resizable(False, False)
for a in record:
    Label(text= a).grid()
exitbutton = Button(text="Exit", command=root.destroy)
exitbutton.grid()
root.mainloop()
