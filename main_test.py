import time
import threading
import customtkinter as ctk
import tkinter
from tkinter import ttk
import tkinter.messagebox

timerup = False
popupstatus = True

def countdown(seconds):
    global timerup
    timerup = True
    seconds *= 1
    while seconds > -1:
        if timerup == False:
            break
        hrs, remainder = divmod(seconds, 3600)  # 3600 seconds in an hour
        mins, secs = divmod(remainder, 60)
        timer = f'{hrs:02}:{mins:02}:{secs:02}'
        if hrs == 0:
            timer = f'{mins:02}:{secs:02}'
        text.config(text=timer)
        seconds -= 1
        time.sleep(1)
    if timerup == False:
        return
    timerup = False
    if popupstatus == True:
        tkinter.messagebox.showinfo("pauza", "čas na pauzu!")
    else:
        text.config(text="čas na pauzu!")

def countdown_start():
    if timerup == False:
        num = field.get()
        if num.isdigit():
            hint.destroy()
        field.delete(0, tkinter.END)
        countdown_thread = threading.Thread(target=countdown,args=(int(num), ))
        countdown_thread.start()
    else:
        plno_thread()

def reset():
    global timerup
    timerup = False
    text.config(text="00:00")

def plno():
    plnotext = ttk.Label(mainframe, text="časovač už běží, zkuste ho vynulovat")
    plnotext.grid(row=2, column=0, pady=10)
    time.sleep(2)
    plnotext.destroy()

def plno_thread():
    plno_thread = threading.Thread(target=plno)
    plno_thread.start()

def popup_off():
    global popupstatus
    popupstatus = False
    popupbutton.config(text="ne", command=popup_on)

def popup_on():
    global popupstatus
    popupstatus = True
    popupbutton.config(text="ano", command=popup_off)

root = ctk.CTk()
root.title("nestůj a pojď")
root.geometry("400x500")
mainframe = tkinter.Frame(root, background="#20242c")
mainframe.pack(fill="both", expand=True)

text = ctk.CTkLabel(mainframe, text="čas se zjeví zde", font=("Brass Mono", 30))
text.grid(row=0, column=0, pady=20)
resetbutton = ctk.CTkButton(mainframe, text="vynulovat", command=reset)
resetbutton.place(x=200, y=200)
#resetbutton.grid(row=0, column=0)

field = ctk.CTkEntry(mainframe, width=50)
field.grid(row=1, column=0, sticky="NWES")
timebutton = ctk.CTkButton(mainframe, text="zapnout", command=countdown_start)
timebutton.grid(row=1, column=1)

hint = ctk.CTkLabel(mainframe, text="zvolte si čas v minutách, celými čísly")
hint.grid(row=2, column=0, pady=10)

popuptext = ctk.CTkLabel(mainframe, text="upozornit na konec časovače pop-upem:")
popuptext.place(x=7, y=173)
popupbutton = ctk.CTkButton(mainframe, text="ano", command=popup_off)
popupbutton.place(x=230, y=170)

root.mainloop()