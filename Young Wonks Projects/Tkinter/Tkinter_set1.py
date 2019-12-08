from tkinter import *

"""creating widgets and putting them on the screen
------------------------------------------------------------------------------
 * label widget (label)
 * tip: 2 button widgets (button and exit_button)
 * tip: must put widgets before the mainloop() command
 * tip: must use pack() to display widgets on screen
"""

##root = Tk()
##label = Label(root, text = "I am a label widget")
##label.pack()
##button = Button(root, text = "I am a button widget")
##button.pack()
##exit_button = Button(root, text = "click to exit", command = exit)
##exit_button.pack()
##root.mainloop()

"""sample tkinter application
------------------------------------------------------------------------------
 * program needs to have 2 labels, 2 entry widgets, and 3 buttons
 * function that grabs text from the entry box and prints it onto the terminal
 * function that deletes text from the entry box
 * functions are called when a button is clicked
"""

##def grabText():
##    enteredtext = entry1.get()
##    print(enteredtext)
##    
##def clearText():
##    entry1.delete(0,END)
##    
##root = Tk()
##
##
##label1 = Label(root, text = "label 1")
##label2 = Label(root, text = "label 2")
##
##entry1 = Entry(root)
##entry2 = Entry(root)
##
##button1 = Button(root, text = "submit", command=grabText)
##button2 = Button(root, text = "clear", command=clearText)
##button3 = Button(root, text = "close", command = exit)
##
##label1.pack()
##label2.pack()
##button1.pack()
##button2.pack()
##button3.pack()
##entry1.pack()
##entry2.pack()
##
##root.mainloop()

"""sample tkinter application 2
------------------------------------------------------------------------------
 * putting labels next to entry boxes
 * root.geometry sets the size of the tkinter window in pixels
"""
##root = Tk()
##
##frame1=Frame(root)
##label1 = Label(frame1, text = "First Name")
##label1.pack(side = LEFT)
##entry1 = Entry(frame1)
##entry1.pack(side = LEFT)
##frame1.pack()

"""sample tkinter application 3
------------------------------------------------------------------------------
 * grid layout(rows and colums)
 * tip: if you dont give a value for a column the value is always 0
 * tip: align the text using N(north),E(east),S(south),W(west) - ex. E = right
 * tip: column span = how many colums the widget to occupies in the tkinter window
 * checkbutton that occupies 2 columns
 * radio button
 * picture
"""
##root = Tk()
##
##
##label1 = Label(root, text = "label 1")
##label2 = Label(root, text = "label 2")
##
##entry1 = Entry(root)
##entry2 = Entry(root)
##
##c = Checkbutton(root, text = "keep me signed in")
##c.grid(columnspan = 4)
##
##radiobutton = Radiobutton(root,text="UP",value=1)
##radiobutton.grid(row=3, column = 1)
##
##photo = PhotoImage(file="copy_of_Plant.png")
##label_3 = Label(root, image=photo)
##label_3.grid(row=3)
##
##label1.grid(row = 0, sticky = E)
##label2.grid(row = 1, sticky = E)
##entry1.grid(row = 0, column = 1)
##entry2.grid(row = 1, column = 1)
##c.grid(row=2, column=2)
##root.mainloop()

"""farenheit to celcius converter
--------------------------------------------------------------------------------
 * farenheit to celcius converter and celcius to fahrenheit converter
 * tip: root.title("title") to set title
 * lambda allows u too pass in arguments
 * tip: if u put at () after function (ex:FtoC()) function runs immediatly and causes an error
"""
##def Convert():
##    if len(str(entry1.get()))== 0:
##        C = int(entry2.get())
##        F = (C*9/5)+32
##        entry1.insert(0,F)
#### the line below checks to see if there is anything in entry 1
##    elif len(str(entry2.get())) == 0:
##        F = int(entry1.get())
##        C = (F-32)*5/9
##        entry2.insert(0,C)
##    else:
##        clearText()
##
##def clearText():
##    entry1.delete(0,END)
##    entry2.delete(0,END)
##    
##
##root = Tk()
##root.title("Farenheit to Celcius")
##
##label1 = Label(root, text = "Farenheit")
##label2= Label(root, text = "Celcius")
##
##entry1 = Entry(root)
##entry2 = Entry(root)
##
##button1 = Button(root, text = "calculate",command=Convert)
##button2 = Button(root, text = "Clear", command=clearText)
##button3 = Button(root, text = "Quit", command=exit)
##
##label1.grid(row=0,column=0)
##label2.grid(row=1,column=0)
##
##entry1.grid(row=0,column=1)
##entry2.grid(row=1,column=1)
##
##button1.grid(row=3,column=0)
##button2.grid(row=3,column=1)
##button3.grid(row=3,column=2)
##
##root.mainloop()

"""Number Guessing Game
------------------------------------------------------------------------------
 * number guessing game
"""
##import random
##from tkinter import messagebox
##number = random.randint(1,100)
##
##def clear():
##    entry1.delete(0,END)
##    
##def guessNumber():
##    guess = entry1.get()
##    if int(guess) == number:
##        messagebox.showinfo('Result','Correct')
##    elif int(guess) > number:
##        messagebox.showinfo('Result','Too high')
##    elif int(guess) < number:
##        messagebox.showinfo('Result','Too low')
##
##root = Tk()
##root.title("Number Guessing Game")
##
##label1 = Label(root, text = "Guess number from (1-100")
##
##button1 = Button(root, text = "Guess number", command = guessNumber)
##button2 = Button(root, text = "Clear", command = clear)
##button3 = Button(root, text = "Exit", command = exit)
##
##entry1 = Entry(root)
##
##label1.grid(row=0,column=0)
##
##button1.grid(row=1,column=0)
##button2.grid(row=1,column=1)
##button3.grid(row=1,column=2)
##
##entry1.grid(row=0,column=1)
##root.mainloop()

"""Signin
------------------------------------------------------------------------------
 * enter the correct username and password to sign in
"""
from tkinter import messagebox
username = "Arty4Lyf"
password = "TrustNo1"
def Login():
    username_guess = entry1.get()
    password_guess = entry2.get()
    if username_guess == username and password_guess == password:
        messagebox.showinfo('Result','Access Granted')
    else:
        messagebox.showinfo('Result','Access Denied')
        entry2.delete(0,END)
        

root = Tk()
root.title("tk")

label1 = Label(root, text = "Username")
label2 = Label(root, text = "Password")

button1 = Button(root, text = "Login", command = Login)

entry1 = Entry(root)
entry2 = Entry(root,show='*')

label1.grid(row=0,column=0)
label2.grid(row=1,column=0)

button1.grid(row=2,column=3)

entry1.grid(row=0,column=1)
entry2.grid(row=1,column=1)


root.mainloop()


