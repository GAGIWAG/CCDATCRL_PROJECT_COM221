import openpyxl
import tkinter as tk
from tkinter import ttk

# Define a Node class for the linked list
class Node:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.next = None

# Define a LinkedList class to manage the linked list
class LinkedList:
    def __init__(self):
        self.head = None
        self.current = None  # Track the current node

    def add_book(self, book_id, title, author):
        new_node = Node(book_id, title, author)
        if self.head is None:
            self.head = new_node
            self.current = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def display_current_book(self):
        if self.current is not None:
            return self.current
        else:
            return None

    def next_book(self):
        if self.current and self.current.next:
            self.current = self.current.next
        return self.display_current_book()

    def previous_book(self):
        prev_node = None
        current_node = self.head

        while current_node and current_node != self.current:
            prev_node = current_node
            current_node = current_node.next

        if prev_node:
            self.current = prev_node
        return self.display_current_book()

    def binary_search(self, target_book_id):
        current = self.head
        while current is not None:
            if current.book_id == target_book_id:
                return current
            elif current.book_id < target_book_id:
                current = current.next
            else:
                return None
        return None

    def search_by_title(self, target_title):
        current = self.head
        while current is not None:
            if target_title.lower() in current.title.lower():
                return current
            current = current.next
        return None

    def search_by_author(self, target_author):
        current = self.head
        while current is not None:
            if target_author.lower() in current.author.lower():
                return current
            current = current.next
        return None

# Load data from the Excel file
def load_data_from_excel(file_path):
    wb = openpyxl.load_workbook(file_path)
    sheet = wb.active
    linked_list = LinkedList()
    for row in sheet.iter_rows(min_row=2, values_only=True):
        book_id, title, author = row[:3]  # Fix here to unpack only 3 values
        linked_list.add_book(book_id, title, author)
    return linked_list

def show_current_book():
    current_book = linked_list.display_current_book()
    if current_book is not None:
        result_label.config(text=f"Book ID: {current_book.book_id}, Title: {current_book.title}, Author: {current_book.author}")
    else:
        result_label.config(text="No books found in the list.")

def next_book():
    next_book = linked_list.next_book()
    if next_book is not None:
        result_label.config(text=f"Book ID: {next_book.book_id}, Title: {next_book.title}, Author: {next_book.author}")
    else:
        result_label.config(text="No more books to display.")

def previous_book():
    previous_book = linked_list.previous_book()
    if previous_book is not None:
        result_label.config(text=f"Book ID: {previous_book.book_id}, Title: {previous_book.title}, Author: {previous_book.author}")
    else:
        result_label.config(text="No previous books to display.")

def search_book():
    search_query = search_entry.get()
    try:
        target_book_id = int(search_query)
        result = linked_list.binary_search(target_book_id)
        if result is not None:
            result_label.config(text=f"Book ID: {result.book_id}, Title: {result.title}, Author: {result.author}")
        else:
            result_label.config(text=f"Book with ID {target_book_id} not found.")
    except ValueError:
        result_label.config(text="Invalid search query. Please enter a valid book ID.")

def search_by_title():
    target_title = title_search_entry.get()
    result = linked_list.search_by_title(target_title)
    if result is not None:
        result_label.config(text=f"Book ID: {result.book_id}, Title: {result.title}, Author: {result.author}")
    else:
        result_label.config(text=f"No books found with title: {target_title}")

def search_by_author():
    target_author = author_search_entry.get()
    result = linked_list.search_by_author(target_author)
    if result is not None:
        result_label.config(text=f"Book ID: {result.book_id}, Title: {result.title}, Author: {result.author}")
    else:
        result_label.config(text=f"No books found by author: {target_author}")

# Create the main window
root = tk.Tk()
root.title("Book Data Display")

# Load data from the Excel file
file_path = "spreadsheets\\books.xlsx"  # Replace with the path to your Excel file
linked_list = load_data_from_excel(file_path)

# Set the default current book to Book ID 1
linked_list.current = linked_list.binary_search(1)

# Create and configure GUI elements
show_button = ttk.Button(root, text="Show Current Book", command=show_current_book)
next_button = ttk.Button(root, text="Next Book", command=next_book)
previous_button = ttk.Button(root, text="Previous Book", command=previous_book)
search_label = ttk.Label(root, text="Search Book ID:")
search_entry = ttk.Entry(root)
search_button = ttk.Button(root, text="Search", command=search_book)
title_search_label = ttk.Label(root, text="Search by Title:")
title_search_entry = ttk.Entry(root)
title_search_button = ttk.Button(root, text="Search Title", command=search_by_title)
author_search_label = ttk.Label(root, text="Search by Author:")
author_search_entry = ttk.Entry(root)
author_search_button = ttk.Button(root, text="Search Author", command=search_by_author)
result_label = ttk.Label(root, text="Result will be displayed here")

# Arrange GUI elements using the grid layout
show_button.grid(row=0, column=0)
next_button.grid(row=0, column=1)
previous_button.grid(row=0, column=2)
search_label.grid(row=1, column=0)
search_entry.grid(row=1, column=1)
search_button.grid(row=1, column=2)
title_search_label.grid(row=2, column=0)
title_search_entry.grid(row=2, column=1)
title_search_button.grid(row=2, column=2)
author_search_label.grid(row=3, column=0)
author_search_entry.grid(row=3, column=1)
author_search_button.grid(row=3, column=2)
result_label.grid(row=4, column=0, columnspan=3)

root.mainloop()
