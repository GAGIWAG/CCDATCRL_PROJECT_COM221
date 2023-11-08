import pandas as pd
import os

# File paths
books_excel_file = 'spreadsheets\\books.xlsx'
usercreds_excel_file = 'spreadsheets\\usercreds.xlsx'

# Hash table to store username and password
user_credentials = {}

# Load existing user credentials from excel
if os.path.exists(usercreds_excel_file):
    dff = pd.read_excel(usercreds_excel_file)
    for index, row in dff.iterrows():
        user_credentials[row['Username']] = row['Password']
        
# Load existing data from Excel
df = pd.read_excel(books_excel_file)
dff = pd.read_excel(usercreds_excel_file)

def save_user_credentials():
    dff = pd.DataFrame(user_credentials.items(), columns=['Username', 'Password'])
    dff.to_excel(usercreds_excel_file, index=False)

def sign_up():
    username = input("Enter a username: ")
    password = input("Enter a password: ")
    user_credentials[username] = password
    save_user_credentials()
    print("Sign-up successful!")

def login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    if username in user_credentials and user_credentials[username] == password:
        print("Login successful!")
        return True
    else:
        print("Invalid username or password.")
        return False

def add_book():
    title = input("Enter the title of the book: ")
    author = input("Enter the author's name: ")

    # Load existing data from excel
    df = pd.read_excel(books_excel_file)

    # Determine the next available Book ID
    next_book_id = len(df) + 1

    # Create a new DataFrame for the book to be added with the determined Book ID
    new_book = pd.DataFrame({'bookID': [next_book_id], 'Title': [title], 'Author': [author]})

    # Concatenate the new book DataFrame with the existing DataFrame
    df = pd.concat([df, new_book], ignore_index=True)

    # Save the updated data to the excel file, overwriting the previous data
    df.to_excel(books_excel_file, index=False)
    save_user_credentials()
    print("Book added successfully!")
    
def select_book():
    title = input("Enter the title of the book you want to select: ")
    
    # Load existing data from excel
    df = pd.read_excel(books_excel_file)

    # If it's not a valid integer, search by title using str.contains for partial and case-insensitive matching
    found_books = df[df['Title'].str.contains(title, case=False)]
    if found_books.empty:
        print("Book not found in the database.")
    else:
        print("Book Details:")


def delete_book():
    title = input("Enter the title of the book to delete: ")

    # Load existing data from excel
    df = pd.read_excel(books_excel_file)

    try:
        # Create a new DataFrame excluding the book to be deleted
        df = df[df['Title'] != title]

        # Save the updated data to the excel file, overwriting the previous data
        df.to_excel(books_excel_file, index=False)
        save_user_credentials()
        print("Book deleted successfully!")
        
    except KeyError:
        print("Book is not in the library!")
        
def save_to_excel():
    # Read data from excel into dff DataFrame
    df = pd.read_excel(books_excel_file)

    # Save the data to the Excel file
    df.to_excel(books_excel_file, index=False)
    save_user_credentials()
    print("Data saved to Excel and user credentials saved to excel successfully!")

def main():
    while True:
        print("\nOptions:")
        print("1. Sign up")
        print("2. Login")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            sign_up()
        elif choice == '2':
            if login():
                while True:
                    print("\nUser Options:")
                    print("1. Add a book")
                    print("2. Select a book")
                    print("3. Delete a book")
                    print("4. Save data to Excel")
                    print("5. Log out")

                    user_choice = input("Enter your choice: ")

                    if user_choice == '1':
                        add_book()
                    elif user_choice == '2':
                        select_book()
                    elif user_choice == '3':
                        delete_book()
                    elif user_choice == '4':
                        save_to_excel()
                    elif user_choice == '5':
                        break
                    else:
                        print("Invalid option.")
        elif choice == '6':
            print("Exiting the program.")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()