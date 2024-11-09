import time
import threading
import tkinter
from tkinter import ttk

def countdown(seconds):
    seconds *= 60
    while seconds > 0:
        hrs, remainder = divmod(seconds, 3600)  # 3600 seconds in an hour
        mins, secs = divmod(remainder, 60)
        timer = f'{hrs:02}:{mins:02}:{secs:02}'
        text.config(text=timer)
        seconds -= 1
        time.sleep(1)

def countdown_start():
    num = field.get()
    countdown_thread = threading.Thread(target=countdown,args=(int(num), ))
    countdown_thread.start()

root = tkinter.Tk()
root.title("Vojtik program")
root.geometry("400x200")
mainframe = tkinter.Frame(root, background="light gray")
mainframe.pack(fill="both", expand=True)

text = ttk.Label(mainframe, text="Time here", font=("Brass Mono", 30))
text.grid(row=0, column=0, pady=20)

field = ttk.Entry(mainframe, width=50)
field.grid(row=1, column=0, sticky="NWES")
button = ttk.Button(mainframe, text="Set time", command=countdown_start)
button.grid(row=1, column=1)



root.mainloop()


    #number = int(input("enter a number "))
    #countdown(number * 60)