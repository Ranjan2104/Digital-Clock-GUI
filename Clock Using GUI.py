# Developed by Amresh Ranjan.

from tkinter import *
from tkinter.ttk import *

from time import strftime

root = Tk()

root.title('Digital Clock using Tkinter GUI')

def clock():
	tick = strftime('%H:%M:%S %p')

	label.config(text =tick)

	label.after(1000, clock)

label = Label(root, font =('sans', 90), background = 'black', foreground = 'yellow')

label.pack(anchor= 'center')

clock()
mainloop()
