import pandas as pd
import os

# File paths
books_excel_file = 'spreadsheets\\books.xlsx'
usercreds_excel_file = 'spreadsheets\\usercreds.xlsx'

# Hash table to store username, email, and password
user_credentials = {}

# Load existing user credentials from excel
if os.path.exists(usercreds_excel_file):
    dff = pd.read_excel(usercreds_excel_file)
    for index, row in dff.iterrows():
        user_credentials[row['Username']] = (row['Email'], row['Password'])

# Function to save user credentials to Excel
def save_user_credentials():
    dff = pd.DataFrame(user_credentials.items(), columns=['Username', 'Email_Password'])
    dff[['Email', 'Password']] = pd.DataFrame(user_credentials.values())
    dff.drop('Email_Password', axis=1, inplace=True)
    dff.to_excel(usercreds_excel_file, index=False)

# Sign-up function to add user credentials
def sign_up():
    email = input("Enter your email: ")
    username = input("Enter a username: ")
    password = input("Enter a password: ")
    user_credentials[username] = (email, password)
    save_user_credentials()
    print("Sign-up successful!")

# Login function to check user credentials
def login():
    username_email = input("Enter your username or email: ")
    password = input("Enter your password: ")
    # Check if username or email and password match the stored credentials
    for stored_username, stored_email, stored_password in user_credentials.items():
        if username_email == stored_username or username_email == stored_email:
            if password == stored_password:
                print("Login successful!")
                return True
    print("Invalid username/email or password.")
    return False

def add_book():
    title = input("Enter the title of the book: ")
    author = input("Enter the author's name: ")
    genre = input("Enter the genre of the book: ")
    theme = input("Enter the theme of the book: ")
    ownership = input("Enter the ownership of the book: ")
    rating = input("Enter the rating of the book: ")
    keywords = input("Enter the possible keywords for the book: ")
    language = input("Enter the language of the book: ")
    awards = input("Enter the awards received by the book: ")
    pubdate = input("Enter the published data of the book: ")

    # Load existing data from excel
    df = pd.read_excel(books_excel_file)

    # Determine the next available Book ID
    next_book_id = len(df) + 1

    # Create a new DataFrame for the book to be added with the determined Book ID
    new_book = pd.DataFrame({'bookID': [next_book_id], 'Title': [title], 'Author': [author], 'Genre': [genre], 'Theme': [theme], 'Ownership': [ownership], 'Rating': [rating], 
    'Keywords': [keywords], 'Language': [language], 'Awards': [awards], 'Publish Date': [pubdate]})

    # Concatenate the new book DataFrame with the existing DataFrame
    df = pd.concat([df, new_book], ignore_index=True)

    # Save the updated data to the excel file, overwriting the previous data
    df.to_excel(books_excel_file, index=False)
    save_user_credentials()
    print("Book added successfully!")
    
def select_book():
    title = input("Enter the title or ID of the book you want to select: ")
    
    # Load existing data from excel
    df = pd.read_excel(books_excel_file)

    # Try to convert the input to an integer (assuming it's an ID)
    try:
        book_id = int(title)
        if book_id < 1 or book_id > len(df):
            print("Invalid book ID.")
            return
        book_info = df.iloc[book_id - 1]
        print("Book Details:")
        print(pd.DataFrame(book_info).transpose().to_string(index=False))  # Display the transposed DataFrame without index
    except ValueError:
        # If it's not a valid integer, search by title using str.contains for partial and case-insensitive matching
        found_books = df[df['Title'].str.contains(title, case=False)]
        if found_books.empty:
            print("Book not found in the database.")
        else:
            print("Book Details:")
            print(found_books.to_string(index=False))  # Display the book details without index

def delete_book():
    title = input("Enter the title of the book to delete: ")

    # Load existing data from excel
    df = pd.read_excel(books_excel_file)

    # Create a new DataFrame excluding the book to be deleted
    df = df[df['title'] != title]

    # Save the updated data to the excel file, overwriting the previous data
    df.to_excel(books_excel_file, index=False)
    save_user_credentials()
    print("Book deleted successfully!")

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
        print("3. Add a book")
        print("4. Delete a book")
        print("5. Save data to Excel")
        print("6. Exit")

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
                        print("Logged out!")
                        break
                    else:
                        print("Invalid option.")
        elif choice == '3':
            print("You need to login first.")
        elif choice == '4':
            print("You need to login first.")
        elif choice == '5':
            print("You need to login first.")
        elif choice == '6':
            print("Exiting the program.")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()