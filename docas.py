import time
import tkinter
from tkinter import ttk

class App():
    def __init__(self):
        self.root = tkinter.Tk()
        self.root.title("Vojtik program")
        self.root.geometry("400x200")
        self.mainframe = tkinter.Frame(self.root, background="light gray")
        self.mainframe.pack(fill="both", expand=True)
        
        self.text = ttk.Label(self.mainframe, text="Hello World", font=("Brass Mono", 30))
        self.text.grid(row=0, column=0, pady=20)

        self.set_text_field = ttk.Entry(self.mainframe, width=50)
        self.set_text_field.grid(row=1, column=0, sticky="NWES")
        self.set_text_button = ttk.Button(self.mainframe, text="Set text", command=self.set_text)
        self.set_text_button.grid(row=1, column=1)

        color_options = ["red", "blue", "white", "gray", "black"]
        self.set_color_field = ttk.Combobox(self.mainframe, width=50, values=color_options)
        self.set_color_field.grid(row=2, column=0, pady=10, sticky="NWES")
        self.set_text_button = ttk.Button(self.mainframe, text="Set color", command=self.set_color)
        self.set_text_button.grid(row=2, column=1, pady=10)    

        self.set_reverse_button = ttk.Button(self.mainframe, text="Reverse changes", command=self.reverse)
        self.set_reverse_button.grid(row=3, column=0, sticky="NWES")

        self.root.mainloop()
        return

    def set_text(self):
        new_text = self.set_text_field.get()
        self.text.config(text=new_text)

    def set_color(self):
        new_color = self.set_color_field.get()
        self.text.config(foreground=new_color)

    def reverse(self):
        self.text.config(text="Hello World", foreground="black")

def countdown(time_sec):
    while time_sec:
        mins, secs = divmod(time_sec, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(timeformat, end='\r')
        time.sleep(1)
        time_sec -= 1

    print("stop")

if __name__ == "__main__":
    App()
    #number = int(input("enter a number "))
    #countdown(number * 60)