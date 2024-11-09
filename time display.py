import time
import threading
import tkinter as tk
from tkinter import ttk

def countdown(time_sec):
    while time_sec:
        mins, secs = divmod(time_sec, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        text.config(text=time_sec)
        time.sleep(1)
        time_sec -= 1

countdown_thread = threading.Thread(target=countdown,args=(5, ))

root = tk.Tk()
root.title("Vojtik program")
root.geometry("400x200")
mainframe = tk.Frame(root, background="light gray")
mainframe.pack(fill="both", expand=True)

text = tk.Label(mainframe, text="cs")
text.grid(row=1,column=0)

countdown_thread.start()

mainframe.mainloop()


