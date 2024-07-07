import os
import tkinter as tk
import datetime
from tkinter import *
from tkinter import ttk
import threading
from functools import partial
from tkinter import font
from data import catalog, section_chosen, section_sep_catalog, section_sep_catalog_jee

closer = False

class Countdown(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.configure(bg='skyblue')
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
        self.label1 = tk.Label(self, width=10, text = '00:00:00', bg='skyblue', font='Times 9 bold')
        self.label2 = tk.Label(self, text='Question number', bg='skyblue')
        self.entry1 = tk.Entry(self, justify = 'center')
        self.entry2 = tk.Entry(self, justify = 'center')
        self.entry1.insert(END, '10800')
        self.entry1.focus_set()
        self.start = tk.Button(self, width=10, text = 'Start', command = self.start_button, bg='gold')
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

def Jee_Mains_timer_submitter_takinganswers():
    '''def value_taker(value):
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
    root.mainloop()'''

    def section_changer(section):
        section_chosen['s'] = section
        sectionlabel['text'] = section_chosen['s']
    def value_taker(value):
        global no_of_questions
        if section_chosen:
            if countdown.entry2.get().isdigit():
                ans = int(countdown.entry2.get())
                if not int(countdown.entry2.get()) > int(no_of_questions):
                    catalog[int(countdown.entry2.get())] = value
                    countdown.entry2.delete(0, 'end')
                    section_sep_catalog_jee[section_chosen['s']][ans] = value
            cc = 1
            for u in section_sep_catalog_jee:
                Label(text=f'{u}', bg='skyblue').grid(row = 10, column=cc)
                cc += 2
                if section_sep_catalog_jee[u]:
                    l = list(section_sep_catalog_jee[u])
                    l.sort()
                    r = 11
                    c = cc - 2
                    for s in l:
                        Label(text=f'{s}:{catalog[s]}', bg='skyblue').grid(row=r, column=c)
                        r += 1
                        if r>35:
                            c +=1
                            r = 11
                
    root = tk.Tk()
    root.title('JEE Exam.....Press Submit exam only when you are done!')
    root.configure(background='skyblue')
    countdown = Countdown(root)
    countdown.grid(column=1, row= 2)
    sectionlabel = Label(text = f'No section Chosen', padx = 35, bg='lawngreen', font='none 11 italic')
    sectionlabel.grid(column=5, row=1)
    mathsbutton = Button(root, text='Maths', padx=25,command=partial(section_changer, 'Maths'), bg='yellow')
    chembutton = Button(root, text='Chem', padx=25,command=partial(section_changer, 'Chem'), bg='yellow')
    physicsbutton = Button(root, text='Physics', padx=25,command=partial(section_changer, 'Physics'), bg='yellow')
    mathsbutton.grid(column=3,row=2)
    chembutton.grid(column=5,row=2)
    physicsbutton.grid(column=7,row=2)
    
    
    abutton = Button(root, text='A', padx=5,command=partial(value_taker,'a'), bg='sandybrown', font='Times 10 bold')
    bbutton = Button(root, text='B', padx=5,command=partial(value_taker,'b'), bg='sandybrown', font='Times 10 bold')
    cbutton = Button(root, text='C', padx=5,command=partial(value_taker,'c'), bg='sandybrown', font='Times 10 bold')
    dbutton = Button(root, text='D', padx=5,command=partial(value_taker,'d'), bg='sandybrown', font='Times 10 bold')
    abutton.grid(column=1, row=6)
    bbutton.grid(column=2, row=6)
    cbutton.grid(column=1, row=7)
    dbutton.grid(column=2, row=7)
    Label(text="Answers :", padx=50, bg='skyblue', font='Times 12 bold', fg='darkgreen').grid(column=1, row=8)
    exitbutton = Button(root, text = 'Submit Exam!', padx= 25,command=root.destroy, bg='orangered', font='Times 11 bold')
    exitbutton.grid(column=2, row=1)
    root.mainloop()


def Bitsat_timer_submitter_takinganswers():
    def section_changer(section):
        section_chosen['s'] = section
        sectionlabel['text'] = section_chosen['s']
    def value_taker(value):
        global no_of_questions
        if section_chosen:
            if countdown.entry2.get().isdigit():
                ans = int(countdown.entry2.get())
                if not int(countdown.entry2.get()) > int(no_of_questions):
                    catalog[int(countdown.entry2.get())] = value
                    countdown.entry2.delete(0, 'end')
                    section_sep_catalog[section_chosen['s']][ans] = value
            cc = 1
            for u in section_sep_catalog:
                Label(text=f'{u}', bg='skyblue').grid(row = 10, column=cc)
                cc += 2
                if section_sep_catalog[u]:
                    l = list(section_sep_catalog[u])
                    l.sort()
                    r = 11
                    c = cc - 2
                    for s in l:
                        Label(text=f'{s}:{catalog[s]}', bg='skyblue').grid(row=r, column=c)
                        r += 1
                        if r>35:
                            c +=1
                            r = 11
                
    root = tk.Tk()
    root.title('Bitsat Exam.....Press Submit exam only when you are done!')
    root.configure(background='skyblue')
    countdown = Countdown(root)
    countdown.grid(column=1, row= 2)
    sectionlabel = Label(text = f'No section Chosen', padx = 35, bg='lawngreen', font='none 11 italic')
    sectionlabel.grid(column=5, row=1)
    mathsbutton = Button(root, text='Maths', padx=25,command=partial(section_changer, 'Maths'), bg='yellow')
    chembutton = Button(root, text='Chem', padx=25,command=partial(section_changer, 'Chem'), bg='yellow')
    physicsbutton = Button(root, text='Physics', padx=25,command=partial(section_changer, 'Physics'), bg='yellow')
    englishbutton = Button(root, text='English', padx=25,command=partial(section_changer, 'English'), bg='yellow')
    logicalreasoningbutton = Button(root, text='Logical Reasoning', padx=35,command=partial(section_changer, 'Logical_Reasoning'), bg='yellow')
    mathsbutton.grid(column=3,row=2)
    chembutton.grid(column=5,row=2)
    physicsbutton.grid(column=7,row=2)
    englishbutton.grid(column=5,row=3)
    logicalreasoningbutton.grid(column=7,row=3)
    
    

    abutton = Button(root, text='A', padx=5,command=partial(value_taker,'a'), bg='sandybrown', font='Times 10 bold')
    bbutton = Button(root, text='B', padx=5,command=partial(value_taker,'b'), bg='sandybrown', font='Times 10 bold')
    cbutton = Button(root, text='C', padx=5,command=partial(value_taker,'c'), bg='sandybrown', font='Times 10 bold')
    dbutton = Button(root, text='D', padx=5,command=partial(value_taker,'d'), bg='sandybrown', font='Times 10 bold')
    abutton.grid(column=1, row=6)
    bbutton.grid(column=2, row=6)
    cbutton.grid(column=1, row=7)
    dbutton.grid(column=2, row=7)
    Label(text="Answers :", padx=50, bg='skyblue', font='Times 12 bold', fg='darkgreen').grid(column=1, row=8)
    exitbutton = Button(root, text = 'Submit Exam!', padx= 25,command=root.destroy, bg='orangered', font='Times 11 bold')
    exitbutton.grid(column=2, row=1)
    root.mainloop()

def report_generator(answers_by_user,answer_key, sectionoof):
    marks = 0
    correct_ans = 0
    question_to_revisit = []
    shitty_ans = []

    for j in answers_by_user:
        try:
            if answers_by_user[j] == answer_key[j]:
                marks += number_for_correct_ans
                correct_ans += 1
            else :
                marks -= 1
                question_to_revisit.append(j)
        except KeyError:
            shitty_ans.append(j)
    
    for j in shitty_ans:
        del answers_by_user[j]

    question_to_revisit.sort()

    quetions_attempted = len(answers_by_user)
    wrong_ans = quetions_attempted - correct_ans
    questions_not_attempted = []

    answer_key_parameters = list(answer_key.keys())

    for k in range(int(answer_key_parameters[0]), int(answer_key_parameters[-1]) + 1):
        if k not in answers_by_user:
            questions_not_attempted.append(k)

    try:
        accuracy = (correct_ans/quetions_attempted) * 100
    except ZeroDivisionError:
        accuracy = 'N.A'


    if sectionoof == 'Overall Report':
        record.extend([f'{sectionoof}', f'Total questions = {len(answer_key)}', f'Marks obtained in mcq = {marks}/300 :\/: +{number_for_correct_ans} for correct ans and -1 for wrong ans',f'Marks obtained in integer type =  /20 :\/: +{number_for_correct_ans} for correct ans and 0 for wrong ans', f'Accuracy = {accuracy} %', f'correct ans = {correct_ans}', f'wrong ans = {wrong_ans}', f'Questions to revisit(questions answered wrong) = {question_to_revisit}', f'Questions not attempted = {questions_not_attempted}\n'])
        return [f'{sectionoof}', f'Total questions = {len(answer_key)}', f'Marks obtained in mcq = {marks}/300 :\/: +{number_for_correct_ans} for correct ans and -1 for wrong ans',f'Marks obtained in integer type =  /20 :\/: +{number_for_correct_ans} for correct ans and 0 for wrong ans', f'Accuracy = {accuracy} %', f'correct ans = {correct_ans}', f'wrong ans = {wrong_ans}', f'Questions to revisit(questions answered wrong) = {question_to_revisit}', f'Questions not attempted = {questions_not_attempted}\n']
    else:
        record.extend([f'{sectionoof}', f'Total questions = {len(answer_key)}', f'Marks obtained = {marks}/{len(answer_key) * number_for_correct_ans} :\/: +{number_for_correct_ans} for correct ans and -1 for wrong ans',f'Marks obtained in integer type =  /20 :\/: +{number_for_correct_ans} for correct ans and 0 for wrong ans', f'Accuracy = {accuracy} %', f'correct ans = {correct_ans}', f'wrong ans = {wrong_ans}', f'Questions to revisit(questions answered wrong) = {question_to_revisit}', f'Questions not attempted = {questions_not_attempted}\n'])
        return [f'{sectionoof}', f'Total questions = {len(answer_key)}', f'Marks obtained = {marks}/{len(answer_key) * number_for_correct_ans} :\/: +{number_for_correct_ans} for correct ans and -1 for wrong ans',f'Marks obtained in integer type =  /20 :\/: +{number_for_correct_ans} for correct ans and 0 for wrong ans', f'Accuracy = {accuracy} %', f'correct ans = {correct_ans}', f'wrong ans = {wrong_ans}', f'Questions to revisit(questions answered wrong) = {question_to_revisit}', f'Questions not attempted = {questions_not_attempted}\n']


    

name = input("Enter your name : ")
date = input("Enter the Date : ")
exam_name = input("Enter the exam name : ")
exam_pattern = int(input('Exam Pattern\n1.)Jee_Mains\n2.)Bitsat\n(1/2):- '))
if exam_pattern not in [1,2]:
    print('Kindly press 1/2 only.......')
    os._exit(0)
if exam_pattern == 1:
    no_of_questions = 90
    number_for_correct_ans = 4
elif exam_pattern == 2:
    no_of_questions = 150
    number_for_correct_ans = 3
while True:
    solution_file = input("Enter the name of the solution file : ")
    solution_file = solution_file + '.txt'
    os.chdir('V:\Python\mcq checker\solution files')
    try :
        with open(f"{solution_file}", 'r') as solutions:
            content = solutions.readlines()
            answer_key = {}

            if exam_pattern == 1:
                for i in range(1, int(no_of_questions) + 1):
                    answer_key[i] = content[0][i-1]
                section_sep_answer_key = {'Maths':{}, 'Chem':{}, 'Physics':{}}
                for i in range(1, 21):
                    section_sep_answer_key['Physics'][i] = content[0][i - 1]
                for i in range(31, 51):
                    section_sep_answer_key['Chem'][i] = content[0][i - 1]
                for i in range(61, 81):
                    section_sep_answer_key['Maths'][i] = content[0][i - 1]


            if exam_pattern == 2:
                for i in range(1, int(no_of_questions) + 1):
                    answer_key[i] = content[0][i - 1]
                section_sep_answer_key = {'Maths':{}, 'Chem':{}, 'Physics':{}, 'Logical_Reasoning':{}, 'English':{}}
                for i in range(1, 41):
                    section_sep_answer_key['Physics'][i] = content[0][i - 1]
                for i in range(41, 81):
                    section_sep_answer_key['Chem'][i] = content[0][i - 1]
                for i in range(81, 96):
                    section_sep_answer_key['English'][i] = content[0][i - 1]
                for i in range(96, 106):
                    section_sep_answer_key['Logical_Reasoning'][i] = content[0][i - 1]
                for i in range(106, 151):
                    section_sep_answer_key['Maths'][i] = content[0][i - 1]
            break
        
    except FileNotFoundError:
        print("Wrong name of the file.")
    except IndexError:
        print("Number of questions according to user are not equal to the number of questions in answer key")

answers_by_user = {}
print('-'*90)
print("Start Now! Mark your clock for 3 hours.")
if exam_pattern == 1:
    Jee_Mains_timer_submitter_takinganswers()
elif exam_pattern == 2:
    Bitsat_timer_submitter_takinganswers()

record = [f'Name - {name}', f'Date - {date}', f'Exam - {exam_name}\n']

x = [f'Name - {name}', f'Date - {date}', f'Exam - {exam_name}\n']

x += report_generator(catalog, answer_key, 'Overall Report')

for t in section_sep_answer_key:
    if exam_pattern == 1:
        report_generator(section_sep_catalog_jee[t], section_sep_answer_key[t], t)
    if exam_pattern == 2:
        report_generator(section_sep_catalog[t], section_sep_answer_key[t], t)

with open('Solution_temp.txt', 'a+') as writer:
    writer.writelines(f'Final Answer list of Date - {date}\n{catalog}\nsection seperated :-\n{section_sep_catalog}\n'+'-'*1024+'\n\n')

os.chdir('V:\Python\mcq checker')

with open('Records.txt', 'a+') as writer:
    for g in record:
        writer.writelines(g + '\n')
    writer.write('-'*90+'\n\n')

root = tk.Tk()
root.title('Report')
root.resizable(False, False)
root.configure(bg='salmon')
Label(root, text="Here's your report.Checkout record text file for section wise brief report.......", bg='salmon').grid()
for a in x:
    Label(root, text= a, bg='salmon').grid()
exitbutton = Button(text="Exit", command=root.destroy, bg='gold')
exitbutton.grid()

root.mainloop()