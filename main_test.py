import time
import tkinter
from tkinter import ttk

def set_text():
    new_text = set_text_field.get()
    text.config(text=new_text)

def set_color():
    new_color = set_color_field.get()
    text.config(foreground=new_color)

def reverse():
    text.config(text="Hello World", foreground="black")

root = tkinter.Tk()
root.title("Vojtik program")
root.geometry("400x200")
mainframe = tkinter.Frame(root, background="light gray")
mainframe.pack(fill="both", expand=True)

text = ttk.Label(mainframe, text="Hello World", font=("Brass Mono", 30))
text.grid(row=0, column=0, pady=20)

set_text_field = ttk.Entry(mainframe, width=50)
set_text_field.grid(row=1, column=0, sticky="NWES")
set_text_button = ttk.Button(mainframe, text="Set text", command=set_text)
set_text_button.grid(row=1, column=1)

color_options = ["red", "blue", "white", "gray", "black"]
set_color_field = ttk.Combobox(mainframe, width=50, values=color_options)
set_color_field.grid(row=2, column=0, pady=10, sticky="NWES")
set_text_button = ttk.Button(mainframe, text="Set color", command=set_color)
set_text_button.grid(row=2, column=1, pady=10)    

set_reverse_button = ttk.Button(mainframe, text="Reverse changes", command=reverse)
set_reverse_button.grid(row=3, column=0, sticky="NWES")

root.mainloop()


def countdown(time_sec):
    while time_sec:
        mins, secs = divmod(time_sec, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(timeformat, end='\r')
        time.sleep(1)
        time_sec -= 1

print("stop")

if __name__ == "__main__":
    __init__()
    #number = int(input("enter a number "))
    #countdown(number * 60)