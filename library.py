import json
import os

# File to save and load library
FILE_NAME = "library.json"

# Load library from file if exists
def load_library():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []

# Save library to file
def save_library(library):
    with open(FILE_NAME, "w") as file:
        json.dump(library, file, indent=4)

# Add a book
def add_book(library):
    title = input("Enter the book title: ").strip()
    author = input("Enter the author: ").strip()
    year = int(input("Enter the publication year: "))
    genre = input("Enter the genre: ").strip()
    read_input = input("Have you read this book? (yes/no): ").strip().lower()
    read_status = True if read_input == "yes" else False

    book = {
        "title": title,
        "author": author,
        "year": year,
        "genre": genre,
        "read": read_status
    }
    library.append(book)
    print("Book added successfully!\n")

# Remove a book
def remove_book(library):
    title = input("Enter the title of the book to remove: ").strip().lower()
    found = False
    for book in library:
        if book["title"].lower() == title:
            library.remove(book)
            print("Book removed successfully!\n")
            found = True
            break
    if not found:
        print("Book not found.\n")

# Search for a book
def search_book(library):
    print("Search by:\n1. Title\n2. Author")
    choice = input("Enter your choice: ")
    keyword = input("Enter the title or author: ").strip().lower()
    results = []
    if choice == "1":
        results = [book for book in library if keyword in book["title"].lower()]
    elif choice == "2":
        results = [book for book in library if keyword in book["author"].lower()]
    else:
        print("Invalid choice.")
        return

    if results:
        print("Matching Books:")
        for i, book in enumerate(results, 1):
            status = "Read" if book["read"] else "Unread"
            print(f"{i}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {status}")
    else:
        print("No matching books found.")
    print()

# Display all books
def display_books(library):
    if not library:
        print("Your library is empty.\n")
        return
    print("Your Library:")
    for i, book in enumerate(library, 1):
        status = "Read" if book["read"] else "Unread"
        print(f"{i}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {status}")
    print()

# Display statistics
def display_stats(library):
    total = len(library)
    read_count = sum(1 for book in library if book["read"])
    percentage = (read_count / total * 100) if total > 0 else 0
    print(f"Total books: {total}")
    print(f"Percentage read: {percentage:.1f}%\n")

# Menu system
def menu():
    library = load_library()
    print("Welcome to your Personal Library Manager!")

    while True:
        print("Menu\n1. Add a book\n2. Remove a book\n3. Search for a book\n4. Display all books\n5. Display statistics\n6. Exit")
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_book(library)
        elif choice == "2":
            remove_book(library)
        elif choice == "3":
            search_book(library)
        elif choice == "4":
            display_books(library)
        elif choice == "5":
            display_stats(library)
        elif choice == "6":
            save_library(library)
            print("Library saved to file. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")

# Run the program
if __name__ == "__main__":
    menu()
