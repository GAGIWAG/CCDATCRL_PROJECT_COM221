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

# Create a function to add 'bookId' and 'Title' to their respective stacks
def add_book_id():
    book_id = book_id_entry.get()
    if book_id:
        book_id_stack.append(book_id)

def add_title():
    title = title_entry.get()
    if title:
        title_stack.append(title)

# Create a function to display the stacks in a GUI
def display_stacks():
    stack_text = f"Book IDs: {', '.join(map(str, book_id_stack))}\nTitles: {', '.join(map(str, title_stack))}"
    text_display.config(state=tk.NORMAL)
    text_display.delete(1.0, tk.END)
    text_display.insert(tk.END, stack_text)
    text_display.config(state=tk.DISABLED)

# Create a Tkinter window
root = tk.Tk()
root.title("Stack Display")

# Create entry widgets to input 'bookId' and 'Title'
book_id_label = tk.Label(root, text="Book ID:")
book_id_label.pack()
book_id_entry = tk.Entry(root)
book_id_entry.pack()

title_label = tk.Label(root, text="Title:")
title_label.pack()
title_entry = tk.Entry(root)
title_entry.pack()

# Create buttons to add 'bookId' and 'Title' to their respective stacks
add_book_id_button = tk.Button(root, text="Add Book ID", command=add_book_id)
add_book_id_button.pack()

add_title_button = tk.Button(root, text="Add Title", command=add_title)
add_title_button.pack()

# Create a Text widget to display the stacks
text_display = tk.Text(root, height=10, width=60)
text_display.pack()

# Create a button to trigger displaying the stacks
display_button = tk.Button(root, text="Display Stacks", command=display_stacks)
display_button.pack()

root.mainloop()
