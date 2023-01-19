import tkinter as tk
def select():
    color = var.get()
    root['bg'] = color

root = tk. Tk()
root.geometry("350x150")
var = tk. StringVar(root)

var.set('red')

choices = ['red', 'green', 'blue', 'yellow','white', 'magenta']
option = tk.OptionMenu(root, var, *choices)

option.pack(side='left', padx=10, pady=10)

button = tk.Button(root, text="check value slected", command=select)
button.pack(side='left', padx=20, pady=10)

root.mainloop()