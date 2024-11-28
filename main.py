import time
import threading
import customtkinter as ctk
import tkinter
from tkinter import ttk
import tkinter.messagebox
import wave
import pyaudio

timerup = False
popupstatus = True
zvukstatus = False

def countdown(seconds):
    global timerup
    timerup = True
    seconds *= 60
    while seconds > -1:
        if timerup == False:
            break
        hrs, remainder = divmod(seconds, 3600)  # 3600 seconds in an hour
        mins, secs = divmod(remainder, 60)
        timer = f'{hrs:02}:{mins:02}:{secs:02}'
        if hrs == 0:
            timer = f'{mins:02}:{secs:02}'
        text.configure(text=timer)
        seconds -= 1
        time.sleep(1)
    if timerup == False:
        return
    timerup = False
    if zvukstatus == True:
        with wave.open("notifikace.wav", 'rb') as wf:
            p = pyaudio.PyAudio()

            stream = p.open(format=p.get_format_from_width(wf.getsampwidth()), channels=wf.getnchannels(), rate=wf.getframerate(), output=True)

            data = wf.readframes(1024)
            while data:
                stream.write(data)
                data = wf.readframes(1024)

            stream.stop_stream()
            stream.close()
            p.terminate()
    if popupstatus == True:
        tkinter.messagebox.showinfo("pauza", "čas na pauzu!")
    else:
        text.configure(text="čas na pauzu!")

def countdown_start():
    if timerup == False:
        num = field.get()
        if num.isdigit():
            hint.configure(text="")
        field.delete(0, tkinter.END)
        countdown_thread = threading.Thread(target=countdown,args=(int(num), ))
        countdown_thread.start()
    else:
        plno_thread()

def reset():
    global timerup
    timerup = False
    text.configure(text="00:00")

def plno():
    hint.configure(text="časovač už běží, zkuste ho vynulovat")
    time.sleep(2)
    hint.configure(text="")

def plno_thread():
    plno_thread = threading.Thread(target=plno)
    plno_thread.start()

def popup_off():
    global popupstatus
    popupstatus = False
    popupbutton.configure(text="ne", command=popup_on)

def popup_on():
    global popupstatus
    popupstatus = True
    popupbutton.configure(text="ano", command=popup_off)

def zvuk_off():
    global zvukstatus
    zvukstatus = False
    zvukbutton.configure(text="ne", command=zvuk_on)

def zvuk_on():
    global zvukstatus
    zvukstatus = True
    zvukbutton.configure(text="ano", command=zvuk_off)

def rezim():
    global root
    if root._fg_color == "#242424":
        root.configure(fg_color="light gray")
        text.configure(text_color="black")
        hint.configure(text_color="black")
        rezimtext.configure(text_color="black")
        zvuktext.configure(text_color="black")
        popuptext.configure(text_color="black")
    else:
        root.configure(fg_color="#242424")
        text.configure(text_color="white")
        hint.configure(text_color="white")
        rezimtext.configure(text_color="white")
        zvuktext.configure(text_color="white")
        popuptext.configure(text_color="white")

root = ctk.CTk()
root.title("nestůj a pojď")
root.geometry("500x500")
root.configure(fg_color="#242424")
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

rezimtext = ctk.CTkLabel(root, text="režim:")
rezimtext.grid(row=12, column=1)
rezimbutton = ctk.CTkButton(root, text="tmavý", command=rezim)
rezimbutton.grid(row=12, column=2)

zvuktext = ctk.CTkLabel(root, text="upozornit na konec časovače zvukem:")
zvuktext.grid(row=13, column=1)
zvukbutton = ctk.CTkButton(root, text="ne", command=zvuk_on)
zvukbutton.grid(row=13, column=2)

popuptext = ctk.CTkLabel(root, text="upozornit na konec časovače pop-upem:")
popuptext.grid(row=14, column=1)
popupbutton = ctk.CTkButton(root, text="ano", command=popup_off)
popupbutton.grid(row=14, column=2)

root.mainloop()