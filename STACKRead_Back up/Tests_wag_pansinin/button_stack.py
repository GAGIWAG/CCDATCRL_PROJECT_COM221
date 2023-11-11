import tkinter as tk
from tkinter import Canvas, Scrollbar
from collections import deque

# Create a stack to store the buttons
button_stack = deque()

# Function to add a button to the frame and the stack
def add_button():
    text = entry.get()
    if text:
        new_button = tk.Button(scrollable_frame, text=text, command=lambda t=text: update_label(t))
        new_button.pack()
        button_stack.append(new_button)

# Function to remove the last added button from the frame and the stack
def remove_button():
    if button_stack:
        removed_button = button_stack.pop()
        removed_button.destroy()

# Function to update the label with the text of the clicked button
def update_label(text):
    label.config(text=text)

# Create the main application window
root = tk.Tk()
root.title("Button App")

# Create a Canvas widget to provide a scrollable area
canvas = Canvas(root)
canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Create a Scrollbar widget and associate it with the canvas
scrollbar = Scrollbar(root, command=canvas.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
canvas.config(yscrollcommand=scrollbar.set)

# Create a frame inside the canvas to hold the buttons
scrollable_frame = tk.Frame(canvas)
canvas.create_window((0, 0), window=scrollable_frame, anchor=tk.NW)

# Bind the canvas to the frame size change
scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

# Create an Entry widget to input text for the new button
entry = tk.Entry(root)
entry.pack()

# Create buttons to add and remove buttons
add_button_btn = tk.Button(root, text="Add Button", command=add_button)
remove_button_btn = tk.Button(root, text="Remove Button", command=remove_button)

add_button_btn.pack()
remove_button_btn.pack()

# Create a label to display the text from the clicked button
label = tk.Label(root, text="")
label.pack()

root.mainloop()
