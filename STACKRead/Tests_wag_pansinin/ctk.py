import tkinter as tk
from time import time

def change_frame_width(new_width):
    frame.config(width=new_width)

def update_width():
    new_width = int(entry.get())
    change_frame_width(new_width)

# Create a tkinter window
window = tk.Tk()
window.geometry("400x200")

# Create a frame
frame = tk.Frame(window, width=200, height=100, bg="blue")
frame.pack()

# Entry for the new width
entry = tk.Entry(window)
entry.pack()

# Button to update the width
update_button = tk.Button(window, text="Update Width", command=update_width)
update_button.pack()

window.mainloop()
