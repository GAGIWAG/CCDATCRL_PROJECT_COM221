import tkinter as tk
from tkinter import Canvas, Scrollbar
from datetime import datetime
import pandas as pd
from collections import deque

# Create a stack to store the buttons
button_stack = deque()

# Create a stack to store the last 10 button data
last_10_stacks = deque(maxlen=10)

# Load data from the Excel file
excel_file_path = "spreadsheets\\books.xlsx"
df = pd.read_excel(excel_file_path)

# Function to add a button to the frame and the stack
def add_button(title, author, rating,genre,theme,keywords):
    text = f"Title: {title}, Author: {author}, Rating: {rating},Genre: {genre}, Theme: {theme}, Keywords: {keywords}"
    new_button = tk.Button(scrollable_frame, text=text, command=lambda t=text: on_button_click(t))
    new_button.pack()
    button_stack.append(new_button)

# Function to remove the last added button from the frame and the stack
def remove_button():
    if button_stack:
        removed_button = button_stack.pop()
        removed_button.destroy()

# Function to handle button click
def on_button_click(text):
    button_data = (text)
    last_10_stacks.append(button_data)
    display_last_10_stacks()

# Function to update the label with the last 10 button data
def display_last_10_stacks():
    update_last_10_buttons()

# Function to update the last 10 buttons
def update_last_10_buttons():
    # Create new buttons for the last 10 button data
    for button_data in last_10_stacks:
        text = button_data
        new_button = tk.Button(last_10_buttons_frame, text=text, command=lambda t=text: print_button_contents(t))
        new_button.pack()
        last_10_buttons.append(new_button)

# Function to print the contents of the clicked button to the label
def print_button_contents(text):
    content_label.config(text=text)
    
def add_button_from_excel(df):
    print("Button Added to Stack")
    
    for index, row in df.iterrows():
        title = row["title"]
        author = row["author"]
        genre = row["rating"]
        theme = row["theme"]
        rating = row["rating"]
        keywords = row["keywords"]
        
        add_button(title, author,genre,theme, rating,keywords)


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

# Create a label to display the last 10 button data
last_10_label = tk.Label(root, text="")
last_10_label.pack()

# Create a frame to hold the last 10 buttons
last_10_buttons_frame = tk.Frame(root)
last_10_buttons_frame.pack()

# List to store the last 10 buttons
last_10_buttons = []

# Create a label to display the contents of the clicked button
content_label = tk.Label(root, text="")
content_label.pack()

add_button_from_excel(df)

root.mainloop()
