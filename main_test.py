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
root.geometry("500x500")
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.columnconfigure(2, weight=1)
root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=1)
root.rowconfigure(2, weight=1)
root.rowconfigure(3, weight=1)
root.rowconfigure(4, weight=1)
root.rowconfigure(5, weight=1)
root.rowconfigure(6, weight=1)
root.rowconfigure(7, weight=1)
root.rowconfigure(8, weight=1)
root.rowconfigure(9, weight=1)
root.rowconfigure(10, weight=1)
root.rowconfigure(11, weight=1)
root.rowconfigure(12, weight=1)
root.rowconfigure(13, weight=1)
root.rowconfigure(14, weight=1)

text = ctk.CTkLabel(root, text="čas se zjeví zde", font=("Brass Mono", 30))
text.grid(row=2, column=1)

resetbutton = ctk.CTkButton(root, text="vynulovat", command=reset)
resetbutton.grid(row=2, column=2)

field = ctk.CTkEntry(root, width=50)
field.grid(row=4, column=1, sticky="NWES")
timebutton = ctk.CTkButton(root, text="zapnout", command=countdown_start)
timebutton.grid(row=4, column=2)

hint = ctk.CTkLabel(root, text="zvolte si čas v minutách, celými čísly")
hint.grid(row=5, column=1)

popuptext = ctk.CTkLabel(root, text="upozornit na konec časovače pop-upem:")
popuptext.grid(row=14, column=1)
popupbutton = ctk.CTkButton(root, text="ano", command=popup_off)
popupbutton.grid(row=14, column=2)

dummycanvas = ctk.CTkEntry(root,width=2000)
dummycanvas.place(x=-10,y=315)

dummytext2 = ctk.CTkLabel(root, text="režim:")
dummytext2.grid(row=12, column=1)
dummytext3 = ctk.CTkLabel(root, text="upozornit na konec časovače zvukem:")
dummytext3.grid(row=13, column=1)

dummybutton2 = ctk.CTkButton(root, text="tmavý")
dummybutton2.grid(row=12, column=2)
dummybutton3 = ctk.CTkButton(root, text="ne")
dummybutton3.grid(row=13, column=2)

root.mainloop()