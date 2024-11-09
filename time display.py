import time
import tkinter as tk
from tkinter import ttk

def countdown(time_sec):
    while time_sec:
        mins, secs = divmod(time_sec, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        #print(timeformat, end='\r')
        text.config(text=timeformat)
        time.sleep(1)
        time_sec -= 1

root = tk.Tk()
root.title("Vojtik program")
root.geometry("400x200")
mainframe = tk.Frame(root, background="light gray")
mainframe.pack(fill="both", expand=True)

text = ttk.Label(mainframe, text="cs")
text.grid(row=0,column=0)

button = ttk.Button(mainframe,text="timer",command=countdown)
button.grid(row=0,column=1)


mainframe.mainloop()

