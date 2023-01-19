from tkinter import *

def volume():
    res= 3.14*int(rl.get())*int(rl.get())*int(hl.get())
    myText.set(res)

def sur_area():
    sur_area = (2*3.14*int(rl.get()) * int(hl.get())) + ((3.14*int(rl.get())**2)*2)
    myText1.set(sur_area )

master = Tk()
master. geometry('500x300')
myText=StringVar()
myText1=StringVar()

Label(master, text="Height of cylinder").grid(row=0)
Label(master, text="Radius of cylinder"). grid(row=1)

Label(master, text="Volume:").grid(row=3)
Label(master, text="sur_area:").grid(row=4)

result=Label(master, text="", textvariable=myText).grid(row=3,column=1)
resultl=Label(master, text="", textvariable=myText1 ).grid(row=4,column=1)

rl = Entry(master)
hl = Entry(master)

rl.grid(row=0, column=1)
hl.grid(row=1, column=1)

b = Button(master, text="Volume", command=volume)
b.grid(row=0, column=2,columnspan=2, rowspan=2, padx=5, pady=5)

c = Button(master, text="Sur_area", command=sur_area)
c.grid(row=3, column=2,columnspan=2, rowspan=2,padx=5, pady=5)

mainloop()