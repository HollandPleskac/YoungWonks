"""Calculator
------------------------------------------------------------------------------
 * Calculator
"""
from tkinter import *
from tkinter import messagebox
import pprint

#first attempt (without try except)
##def Addition():
##    if len(str(entry1.get())) != 0 and len(str(entry2.get())) != 0:
##        firstnum = int(entry1.get())
##        secondnum = int(entry2.get())
##        total = firstnum+secondnum
##        entry3.delete(0,END)
##        entry3.insert(0,total)
def Addition():
    try:
        var = float(entry1.get()) + float(entry2.get())
        res.set(var)
    except:
        messagebox.showerror('Error',"Invalid Input")

def Subtraction():
    try:
        var = float(entry1.get()) - float(entry2.get())
        res.set(var)
    except:
        messagebox.showerror('Error',"Invalid Input")
    
def Multiplication():
    try:
        var = float(entry1.get()) * float(entry2.get())
        res.set(var)
    except:
        messagebox.showerror('Error',"Invalid Input")

def Division():
    try:
        var = float(entry1.get()) / float(entry2.get())
        res.set(var)
    except:
        messagebox.showerror('Error',"Invalid Input")
        

    
root=Tk()
root.title("CALCULATOR")
root.geometry("400x150")
root.resizable(width=False, height=False)

color='gray'
num1 = IntVar()
num2 = IntVar()
res = IntVar()

frame1 = Frame(root, bg=color)
frame2 = Frame(root, bg=color)
frame3 = Frame(root, bg=color)
frame4 = Frame(root, bg=color)

frame1.pack(expand=1, fill=BOTH)
frame2.pack(expand=1, fill=BOTH)
frame3.pack(expand=1, fill=BOTH)
frame4.pack(expand=1, fill=BOTH)

button1 = Button(frame3, text = "+", command=Addition)
button2 = Button(frame3, text = "-", command=Subtraction)
button3 = Button(frame3, text = "*", command=Multiplication)
button4 = Button(frame3, text = "/", command=Division)


label1 = Label(frame1 , text = 'Input Number 1 :', bg = color)
label2 = Label(frame2 , text = 'Input Number 2 :', bg = color)
label3 = Label(frame4 , text = 'Result :', bg = color)

entry1 = Entry(frame1 , highlightbackground=color , textvariable=num1)
entry2 = Entry(frame2 , highlightbackground=color , textvariable=num2)
entry3 = Entry(frame4 , highlightbackground=color , textvariable=res)

button1.pack(side=LEFT, padx=5, pady=5)
button2.pack(side=LEFT, padx=5, pady=5)
button3.pack(side=LEFT, padx=5, pady=5)
button4.pack(side=LEFT, padx=5, pady=5)

button1.config(height=1, width=12)
button2.config(height=1, width=12)
button3.config(height=1, width=12)
button4.config(height=1, width=12)

label1.pack(side=LEFT)
label2.pack(side=LEFT)
label3.pack(side=LEFT)

entry1.pack(side=RIGHT)
entry2.pack(side=RIGHT)
entry3.pack(side=RIGHT)
