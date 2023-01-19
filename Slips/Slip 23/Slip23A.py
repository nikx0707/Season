import tkinter as tk
win = tk.Tk()
win.geometry("650x250")

def size_1():
    text.config(font=('Arial',20))
    text.config(bg= 'gray51', fg= "white")

def size_2():
    text.config(font=('Helvetica bold',40))
    text.config(bg= "white", fg= "red")

text=Label(win, text="Hello World!")
text.pack()

frame= Frame(win)

Label(frame, text="Select the Font-Size").pack()
                  
buttonl= Checkbutton(frame, text='Arial - 20', command= size_1)
buttonl.pack(pady=10)

button2= Checkbutton(frame, text='Helvetica - 40', command=size_2)

button2.pack(pady=10)

frame.pack()

win.mainloop()