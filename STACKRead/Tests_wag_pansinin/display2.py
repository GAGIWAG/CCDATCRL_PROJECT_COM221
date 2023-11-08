import openpyxl
import tkinter as tk
from tkinter import ttk

# Create an empty list to store data
data_list = []

# Replace 'your_excel_file.xlsx' with the path to your Excel file
excel_file = 'spreadsheets\\books.xlsx'

# Load the Excel file
workbook = openpyxl.load_workbook(excel_file)

# Choose a specific sheet within the Excel file, e.g., the first sheet
sheet = workbook.active

# Use a variable to skip the first row (headers)
skip_first_row = True

# Iterate through the rows in the sheet and add data to the list
for row in sheet.iter_rows(values_only=True):
    if skip_first_row:
        skip_first_row = False
        continue

    book_info = {
        'book_id': row[0],
        'title': row[1],
        'author': row[2]
    }
    data_list.append(book_info)

# Create a function to display the list in the Treeview
def display_list_as_treeview():
    # Clear any existing items
    treeview.delete(*treeview.get_children())

    # Insert data into the Treeview
    for i, book_info in enumerate(data_list, start=1):
        treeview.insert('', 'end', values=(i, book_info['title'], book_info['author']))

# Create a Tkinter window
root = tk.Tk()
root.title("Stack Display")

# Create a frame to hold the Treeview and scrollbars
frame = ttk.Frame(root)
frame.pack(fill='both', expand=True)

# Create a Treeview widget
columns = ('#', 'Title', 'Author')
treeview = ttk.Treeview(frame, columns=columns, show='headings')
treeview.heading('#1', text='#')
treeview.heading('#2', text='Title')
treeview.heading('#3', text='Author')

# Create vertical and horizontal scrollbars
vsb = ttk.Scrollbar(frame, orient='vertical', command=treeview.yview)
hsb = ttk.Scrollbar(frame, orient='horizontal', command=treeview.xview)
treeview.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

# Pack the Treeview and scrollbars
treeview.pack(side='left', fill='both', expand=True)
vsb.pack(side='right', fill='y')
hsb.pack(side='bottom', fill='x')

# Create a button to trigger displaying the list in the Treeview
display_button = ttk.Button(root, text="Display List as Treeview", command=display_list_as_treeview)
display_button.pack()

root.mainloop()
