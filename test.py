import threading
import time
import tkinter as tk
from tkinter import ttk

def countdown(time_sec):
    while time_sec:
        mins, secs = divmod(time_sec, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(timeformat)
        time_sec -= 1
        time.sleep(1)

def hello():
    for i in range(5):
        print("Hello World")
        time.sleep(1)

countdown_thread = threading.Thread(target=countdown,args=(5, ))
hello_thread = threading.Thread(target=hello)

countdown_thread.start()
hello_thread.start()




"""
def countdown(time_sec):
    while time_sec:
        mins, secs = divmod(time_sec, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(timeformat, end='\r')
        text.config(text=time_sec)
        time.sleep(1)
        time_sec -= 1


root = tk.Tk()
root.title("Vojtik program")
root.geometry("400x200")
mainframe = tk.Frame(root, background="light gray")
mainframe.pack(fill="both", expand=True)

text = tk.Label(mainframe, text="cs")
text.grid(row=1,column=0)


mainframe.mainloop()

countdown(30)
"""