import pandas as pd
import tkinter as tk
import customtkinter
from tkinter import Button, Frame, Scrollbar, Canvas

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot] 
    return quicksort(left) + middle + quicksort(right)

def display_buttons(frame, df):
    # Create buttons for each row and display them in the GUI
    for index, row in df.iterrows():
        button_text = f"{row['title']} by {row['author']} | {row['rating']}"
        button = customtkinter.CTkButton(frame, text=button_text,width=450)
        button.pack(padx=10, pady=5)

def sort_ascending(frame, df):
    # Sort in ascending order
    sorted_df = df.sort_values(by='rating')
    update_display(frame, sorted_df)

def sort_descending(frame, df):
    # Sort in descending order
    sorted_df = df.sort_values(by='rating', ascending=False)
    update_display(frame, sorted_df)

def update_display(frame, df):
    # Display the sorted buttons
    display_buttons(frame, df)

root = customtkinter.CTk()
root.title("Sorted rating")

# Read the Excel file into a pandas DataFrame
file_path = "spreadsheets\\books.xlsx"  # Replace with the path to your Excel file
df = pd.read_excel(file_path)

# Create a frame for sorting buttons
sort_frame = customtkinter.CTkFrame(root)
sort_frame.pack(side=tk.TOP, padx=10, pady=10)

sort_asc_button = customtkinter.CTkButton(sort_frame, text="Sort Ascending", command=lambda: sort_ascending(scrollable_frame, df))
sort_asc_button.pack(side=tk.LEFT)

sort_desc_button = customtkinter.CTkButton(sort_frame, text="Sort Descending", command=lambda: sort_descending(scrollable_frame, df))
sort_desc_button.pack(side=tk.LEFT, padx=10)

scrollable_frame = customtkinter.CTkScrollableFrame(root,width=450)
scrollable_frame.pack()

# Display unsorted buttons
display_buttons(scrollable_frame, df)

root.mainloop()

