import openpyxl
import customtkinter

# Create an empty stack to store data
stack = []

# Replace 'your_excel_file.xlsx' with the path to your Excel file
excel_file = 'spreadsheets\\books.xlsx'

# Load the Excel file
workbook = openpyxl.load_workbook(excel_file)

# Choose a specific sheet within the Excel file, e.g., the first sheet
sheet = workbook.active

# Use a variable to skip the first row (headers)
skip_first_row = True

# Iterate through the rows in the sheet and add data to the stack
for row in sheet.iter_rows(values_only=True):
    if skip_first_row:
        skip_first_row = False
        continue

    book_info = {
        'book_id': row[0],
        'title': row[1],
        'author': row[2],
        'genre': row[3],
        'keywords': row[4],         
        'rating': row[5]
        }  
    stack.append(book_info)

# Create a function to display the details of the selected book
def display_book_details(book_info):
    book_id_label.configure(text=f"Book ID: {book_info['book_id']}")
    title_label.configure(text=f"Title: {book_info['title']}")
    author_label.configure(text=f"Author: {book_info['author']}")
    genre_label.configure(text=f"Genre: {book_info['genre']}")
    keywords_label.configure(text=f"Keyword: {book_info['keywords']}")
    rating_label.configure(text=f"Rating: {book_info['genre']}")

# Create a function to display the stack as buttons in a scrollable frame
def display_stack_as_buttons():
    # Create a canvas with a vertical scrollbar
    canvas = customtkinter.CTkCanvas(scrollable_frame, width=520, height=400)
    canvas.pack(side="left", fill="both", expand=True)

    scrollbar = customtkinter.CTkScrollbar(scrollable_frame, command=canvas.yview)
    scrollbar.pack(side="right", fill="y")

    canvas.configure(yscrollcommand=scrollbar.set)

    # Create buttons for each book in the stack and add them to the frame
    for book_info in stack:
        book_button = customtkinter.CTkButton(canvas,width=520,hover_color="#3D291E",fg_color="#614D40",height=25, text=f"{book_info['title']} \nby {book_info['author']}", command=lambda info=book_info: display_book_details(info),corner_radius=0)
        book_button.pack(pady=1)

    # Configure the canvas to scroll the frame
    canvas.configure(scrollregion=canvas.bbox("all"))

app = customtkinter.CTk()
app.geometry("550x500")
app.title("CTk example")

# Create a canvas to hold the scrollable frame
canvas = customtkinter.CTkCanvas(app)
canvas.pack(side="top", fill="both", expand=True)

scrollable_frame = customtkinter.CTkScrollableFrame(canvas, width=520, height=410)
scrollable_frame.place(x=0,y=0)

# Create labels to display book details
book_id_label = customtkinter.CTkLabel(app, text="")
book_id_label.pack()
title_label = customtkinter.CTkLabel(app, text="")
title_label.pack()
author_label = customtkinter.CTkLabel(app, text="")
author_label.pack()
genre_label = customtkinter.CTkLabel(app, text="")
genre_label.pack()
keywords_label = customtkinter.CTkLabel(app, text="")
keywords_label.pack()
rating_label = customtkinter.CTkLabel(app, text="")
rating_label.pack()

display_stack_as_buttons()


app.mainloop()