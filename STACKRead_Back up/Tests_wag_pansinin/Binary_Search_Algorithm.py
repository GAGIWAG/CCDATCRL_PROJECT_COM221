import openpyxl
import tkinter as tk
from tkinter import ttk

# Define a Node class for the linked list
class Node:
    def __init__(self, book_id, title, author, genre, theme, ownership, rating, keywords, language, awards, publish_date):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.genre = genre
        self.theme = theme
        self.ownership = ownership
        self.rating = rating
        self.keywords = keywords
        self.language = language
        self.awards = awards
        self.publish_date = publish_date
        self.next = None

# Define a LinkedList class to manage the linked list
class LinkedList:
    def __init__(self):
        self.head = None
        self.current = None  # Track the current node

    def add_book(self, book_id, title, author, genre, theme, ownership, rating, keywords, language, awards, publish_date):
        new_node = Node(book_id, title, author, genre, theme, ownership, rating, keywords, language, awards, publish_date)
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
        results = []
        while current is not None:
            if target_title.lower() in current.title.lower():
                results.append(current)
            current = current.next
        return results

    def search_by_author(self, target_author):
        current = self.head
        results = []
        while current is not None:
            if target_author.lower() in current.author.lower():
                results.append(current)
            current = current.next
        return results

    def search_by_attribute(self, target_attribute, attribute_name):
        current = self.head
        results = []
        while current is not None:
            if target_attribute.lower() in str(getattr(current, attribute_name)).lower():
                results.append(current)
            current = current.next
        return results

# Load data from the Excel file
def load_data_from_excel(file_path):
    wb = openpyxl.load_workbook(file_path)
    sheet = wb.active
    linked_list = LinkedList()
    for row in sheet.iter_rows(min_row=2, values_only=True):
        book_id, title, author, genre, theme, ownership, rating, keywords, language, awards, publish_date = row
        linked_list.add_book(book_id, title, author, genre, theme, ownership, rating, keywords, language, awards, publish_date)
    return linked_list

def show_current_book():
    current_book = linked_list.display_current_book()
    if current_book is not None:
        result_label.config(text=f"Book ID: {current_book.book_id}\nTitle: {current_book.title}\nAuthor: {current_book.author}\nGenre: {current_book.genre}\nTheme: {current_book.theme}\nOwnership: {current_book.ownership}\nRating: {current_book.rating}\nKeywords: {current_book.keywords}\nLanguage: {current_book.language}\nAwards: {current_book.awards}\nPublish Date: {current_book.publish_date}")
    else:
        result_label.config(text="No books found in the list.")

def next_book():
    next_book = linked_list.next_book()
    if next_book is not None:
        result_label.config(text=f"Book ID: {next_book.book_id}\nTitle: {next_book.title}\nAuthor: {next_book.author}\nGenre: {next_book.genre}\nTheme: {next_book.theme}\nOwnership: {next_book.ownership}\nRating: {next_book.rating}\nKeywords: {next_book.keywords}\nLanguage: {next_book.language}\nAwards: {next_book.awards}\nPublish Date: {next_book.publish_date}")
    else:
        result_label.config(text="No more books to display.")

def previous_book():
    previous_book = linked_list.previous_book()
    if previous_book is not None:
        result_label.config(text=f"Book ID: {previous_book.book_id}\nTitle: {previous_book.title}\nAuthor: {previous_book.author}\nGenre: {previous_book.genre}\nTheme: {previous_book.theme}\nOwnership: {previous_book.ownership}\nRating: {previous_book.rating}\nKeywords: {previous_book.keywords}\nLanguage: {previous_book.language}\nAwards: {previous_book.awards}\nPublish Date: {previous_book.publish_date}")
    else:
        result_label.config(text="No previous books to display.")

def display_search_results(results):
    # Create a new frame to display search results as buttons
    results_frame = ttk.Frame(root)
    results_frame.grid(row=2, column=0, columnspan=3)

    # Create buttons for each result
    for book in results:
        button_text = f"{book.title} - {book.author}"
        ttk.Button(results_frame, text=button_text, command=lambda b=book: display_book_details(b)).pack()

def display_book_details(book):
    # Display details of the selected book
    result_label.config(text=f"Book ID: {book.book_id}\nTitle: {book.title}\nAuthor: {book.author}\nGenre: {book.genre}\nTheme: {book.theme}\nOwnership: {book.ownership}\nRating: {book.rating}\nKeywords: {book.keywords}\nLanguage: {book.language}\nAwards: {book.awards}\nPublish Date: {book.publish_date}")

def search():
    search_query = search_entry.get()
    
    try:
        target_book_id = int(search_query)
        result = linked_list.binary_search(target_book_id)
        if result is not None:
            result_label.config(text=f"Book ID: {result.book_id}\nTitle: {result.title}\nAuthor: {result.author}\nGenre: {result.genre}\nTheme: {result.theme}\nOwnership: {result.ownership}\nRating: {result.rating}\nKeywords: {result.keywords}\nLanguage: {result.language}\nAwards: {result.awards}\nPublish Date: {result.publish_date}")
        else:
            result_label.config(text=f"Book with ID {target_book_id} not found.")
    except ValueError:
        # Check for Title, Author, and attributes
        result = linked_list.search_by_title(search_query)
        if result is None:
            result = linked_list.search_by_author(search_query)
            if result is None:
                result = linked_list.search_by_attribute(search_query, "genre")
                if result is None:
                    result = linked_list.search_by_attribute(search_query, "theme")
                    if result is None:
                        result = linked_list.search_by_attribute(search_query, "ownership")
                        if result is None:
                            result = linked_list.search_by_attribute(search_query, "rating")
                            if result is None:
                                result = linked_list.search_by_attribute(search_query, "keywords")
                                if result is None:
                                    result = linked_list.search_by_attribute(search_query, "language")
                                    if result is None:
                                        result = linked_list.search_by_attribute(search_query, "awards")
                                        if result is None:
                                            result = linked_list.search_by_attribute(search_query, "publish_date")
                
        if result:
            display_search_results(result)
        else:
            result_label.config(text=f"No books found for the search query: {search_query}")

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
search_label = ttk.Label(root, text="Search:")
search_entry = ttk.Entry(root)
search_button = ttk.Button(root, text="Search", command=search)
result_label = ttk.Label(root, text="Result will be displayed here")

# Arrange GUI elements using the grid layout
show_button.grid(row=0, column=0)
next_button.grid(row=0, column=1)
previous_button.grid(row=0, column=2)
search_label.grid(row=1, column=0)
search_entry.grid(row=1, column=1)
search_button.grid(row=1, column=2)
result_label.grid(row=2, column=0, columnspan=3)

root.mainloop()
