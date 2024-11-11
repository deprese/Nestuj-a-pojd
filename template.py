import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Vojtik program")
root.geometry("400x200")
mainframe = tk.Frame(root, background="light gray")
mainframe.pack(fill="both", expand=True)

text = ttk.Label(mainframe, text="Hello World", font=("Brass Mono", 30))
text.grid(row=0, column=0, pady=20, padx=20)

top = tk.Toplevel(mainframe)

mainframe.mainloop()