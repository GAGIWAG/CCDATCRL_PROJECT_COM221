import tkinter as tk
from tkinter import Canvas, Scrollbar
import pandas as pd
from collections import deque

# Create a stack to store the buttons
button_stack = deque()

# Create a linked list to store the last 10 rows from the "books" Excel file
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self, limit=10):
        self.head = None
        self.limit = limit

    def append(self, data):
        # Check if the value is already present
        if self.search(data):
            return

        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next

            current.next = new_node

            # Remove the first item if the limit is reached
            if self.count() > self.limit:
                self.head = self.head.next

    def search(self, value):
        current = self.head
        while current:
            if current.data == value:
                return True
            current = current.next
        return False

    def count(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    def display(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next

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

# Function to update the label with the text of the clicked button and append to the linked list
def update_label(text):
    label.config(text=text)
    last_10_rows.append(text)
    display_last_10_rows()

# Function to display the contents of the linked list as buttons
def display_last_10_rows():
    # Clear existing buttons
    for widget in last_10_rows_frame.winfo_children():
        widget.destroy()

    current = last_10_rows.head
    while current:
        new_button = tk.Button(last_10_rows_frame, text=current.data)
        new_button.pack()
        current = current.next

# Read data from the "books.xlsx" file using pandas
df = pd.read_excel("spreadsheets\\books.xlsx")

# Create the main application window
root = tk.Tk()
root.title("Book App")

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

# Create a frame to display the last 10 rows
last_10_rows_frame = tk.Frame(root)
last_10_rows_frame.pack()

# Create a linked list to store the last 10 rows with a limit of 10
last_10_rows = LinkedList(limit=10)

# Append each row as a single string to the linked list
for index, row in df.iterrows():
    row_str = ', '.join([f"{col}: {value}" for col, value in row.items()])
    last_10_rows.append(row_str)

root.mainloop()
