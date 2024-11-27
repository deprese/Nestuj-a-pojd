import tkinter as tk

# Create the main window
root = tk.Tk()
root.geometry('300x200')  # Set the window size

# Create a label widget
label = tk.Label(root, text="Centered Label")

# Configure grid to center the label
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.columnconfigure(2, weight=1)
label.grid(row=0, column=1)

# Run the application
root.mainloop()