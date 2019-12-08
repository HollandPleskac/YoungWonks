"""Food Price Calculator
------------------------------------------------------------------------------
 * Food Price Calculator
"""
from tkinter import *

apple_price=120
bananna_price=450
orange_price=310
def calculatePrice(x):
    entry1.delete(0,END)
    item=var.get()
    
    entry1.insert(0,int(x)*item)

root = Tk()

root.title("Food Price Calculator")
root.geometry("300x200")
root.resizable(width=False, height=False)

color='gray'

frame1 = Frame(root, bg='blue')
frame2 = Frame(root, bg='red')
frame3 = Frame(root, bg='gray')

label1 = Label(root, text = "Choose an Item", bg=color)
label2 = Label(frame2, text = "Price", bg=color)

var=IntVar()
print(var)
radio_btn1 = Radiobutton(frame1, text= "Apple", variable=var, bg = color, value = 12)
radio_btn2 = Radiobutton(frame1, text= "Bannana",variable=var, bg = color, value = 35)
radio_btn3 = Radiobutton(frame1, text= "Orange",variable=var, bg = color, value = 22)

entry1 = Entry(frame2, width=25)
entry2 = Entry(frame3, width=25)

button1 = Button(frame3, text = "cal", command= lambda:calculatePrice(entry2.get()))

label1.place(x=100, y=5)
frame1.pack(expand=1, fill=BOTH)
frame2.pack(expand=1, fill=BOTH)
frame3.pack(expand=1, fill=BOTH)

radio_btn1.grid(row=0,column=0)
radio_btn2.grid(row=1,column=0)
radio_btn3.grid(row=2,column=0)

label2.grid(row=0,column=0)
entry1.grid(row=0,column=1)

button1.grid(row=0,column=0)
entry2.grid(row=0,column=1)

root.mainloop()
