import openpyxl
import tkinter as tk

# Create empty stacks to store 'bookId' and 'Title'
book_id_stack = []
title_stack = []

# Replace 'your_excel_file.xlsx' with the path to your Excel file
excel_file = 'spreadsheets\\books.xlsx'

# Load the Excel file
workbook = openpyxl.load_workbook(excel_file)

# Choose a specific sheet within the Excel file, e.g., the first sheet
sheet = workbook.active

# Flag to skip the first row
skip_first_row = True

# Iterate through the rows in the sheet, skipping the first row
for row in sheet.iter_rows(values_only=True):
    if skip_first_row:
        skip_first_row = False
        continue

    book_id, title = row[0], row[1]
    if book_id is not None and title is not None:
        book_id_stack.append(book_id)
        title_stack.append(title)

# Create a function to display the stacks in their respective frames
def display_stacks():
    for i in range(len(book_id_stack)):
        book_id = book_id_stack[i]
        title = title_stack[i]

        book_id_button = tk.Button(book_id_frame, text=f"Book ID: {book_id}", command=lambda id=book_id: display_selected(id))
        title_button = tk.Button(title_frame, text=f"Title: {title}", command=lambda t=title: display_selected(t))

        book_id_button.pack(padx=5, pady=10)
        title_button.pack()

def display_selected(value):
    selected_text.set(value)

# Create a Tkinter window
root = tk.Tk()
root.title("Stack Display")

# Create a Text widget to display the selected item
selected_text = tk.StringVar()
selected_label = tk.Label(root, textvariable=selected_text)
selected_label.pack()

# Create a frame for 'bookId' buttons
book_id_frame = tk.Frame(root)
book_id_frame.pack(side=tk.LEFT, padx=10)

# Create a frame for 'Title' buttons
title_frame = tk.Frame(root)
title_frame.pack(side=tk.RIGHT, padx=10)

# Create a button to trigger displaying the stacks
display_button = tk.Button(root, text="Display Stacks", command=display_stacks)
display_button.pack()

root.mainloop()
