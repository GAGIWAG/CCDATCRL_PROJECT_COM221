import pandas as pd
import tkinter as tk
from tkinter import Button, Frame, Scrollbar, Canvas, Label

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

def display_buttons(frame, df, on_button_click):
    # Create buttons for each row and display them in the GUI
    for index, row in df.iterrows():
        button_text = f"{row['title']} by {row['author']} - {row['rating']}"
        button = Button(frame, text=button_text, padx=10, pady=5, command=lambda text=button_text: on_button_click(text))
        button.pack()

def sort_ascending(frame, df, on_button_click):
    # Sort in ascending order
    sorted_df = df.sort_values(by='rating')
    update_display(frame, sorted_df, on_button_click)

def sort_descending(frame, df, on_button_click):
    # Sort in descending order
    sorted_df = df.sort_values(by='rating', ascending=False)
    update_display(frame, sorted_df, on_button_click)

def update_display(frame, df, on_button_click):
    # Clear previously displayed buttons
    for widget in frame.winfo_children():
        widget.destroy()

    # Display the sorted buttons
    display_buttons(frame, df, on_button_click)

def on_frame_configure(canvas, event):
    canvas.configure(scrollregion=canvas.bbox("all"))

def on_canvas_configure(canvas, event):
    canvas.itemconfig("self.scrollable_frame", width=event.width)

def on_button_click(text, label):
    # Display the content of the clicked button in the label
    label.config(text=f"Clicked button: {text}")

def main():
    root = tk.Tk()
    root.title("Sorted rating")

    # Read the Excel file into a pandas DataFrame
    file_path = "spreadsheets\\books.xlsx"  # Replace with the path to your Excel file
    df = pd.read_excel(file_path)

    # Create a label to display the clicked button content
    clicked_label = Label(root, text="", pady=10)
    clicked_label.pack()

    # Create a frame for sorting buttons
    sort_frame = Frame(root)
    sort_frame.pack(side=tk.TOP, padx=10, pady=10)

    sort_asc_button = Button(sort_frame, text="Sort Ascending", command=lambda: sort_ascending(scrollable_frame, df, lambda text: on_button_click(text, clicked_label)))
    sort_asc_button.pack(side=tk.LEFT)

    sort_desc_button = Button(sort_frame, text="Sort Descending", command=lambda: sort_descending(scrollable_frame, df, lambda text: on_button_click(text, clicked_label)))
    sort_desc_button.pack(side=tk.LEFT, padx=10)

    # Create a scrollable frame for the stack of buttons
    canvas = Canvas(root, borderwidth=0, background="#ffffff")
    scrollbar = Scrollbar(root, orient="vertical", command=canvas.yview)
    scrollable_frame = Frame(canvas)

    canvas.configure(yscrollcommand=scrollbar.set)

    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw", tags="self.scrollable_frame")

    scrollable_frame.bind("<Configure>", lambda event: on_frame_configure(canvas, event))
    canvas.bind("<Configure>", lambda event: on_canvas_configure(canvas, event))

    # Display unsorted buttons
    display_buttons(scrollable_frame, df, lambda text: on_button_click(text, clicked_label))

    root.mainloop()

if __name__ == "__main__":
    main()
