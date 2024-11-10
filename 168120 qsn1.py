class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

    def mark_as_borrowed(self):
        if not self.is_borrowed:
            self.is_borrowed = True
            print(f"'{self.title}' by {self.author} has been marked as borrowed")
        else:
            print(f"'{self.title}' is already borrowed.")

    def mark_as_returned(self):
        if self.is_borrowed:
            self.is_borrowed = False
            print(f"'{self.title}' has been marked as returned.")
        else:
            print(f"'{self.title}' was not borrowed.")


class LibraryMember:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []

    def borrow_book(self, book):
        if not book.is_borrowed:
            book.mark_as_borrowed()
            self.borrowed_books.append(book)
            print(f"{self.name} has borrowed '{book.title}'.")
        else:
            print(f"Sorry, '{book.title}' is currently borrowed by someone else.")

    def return_book(self, book):
        if book in self.borrowed_books:
            book.mark_as_returned()
            self.borrowed_books.remove(book)
            print(f"{self.name} has returned '{book.title}'.")
        else:
            print(f"{self.name} has not borrowed '{book.title}'.")

    def list_borrowed_books(self):
        if self.borrowed_books:
            print(f"{self.name} has borrowed the following books:")
            for book in self.borrowed_books:
                print(f"- {book.title} by {book.author}")
        else:
            print(f"{self.name} has not borrowed any books.")


def main():
    book1 = Book("Entreprenuership", "Alvin Majawa")
    book2 = Book("World War I", "Elsie Nyambura")
    book3 = Book("The Great Wall Of China", "F. Nyaga Gucheru")

    member = LibraryMember("Gladys Njoki", "M001")
    books = [book1, book2, book3]

    while True:
        print("\n\t\t\t\tWelcome to Our Library Management System\n\nEnter an option Number below.")
        print("1. Borrow a book")
        print("2. Return a book")
        print("3. List borrowed books")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            print("\n\nBelow are the Available books:")
            available_books = [book for book in books if not book.is_borrowed]
            if available_books:
                for book in available_books:
                    print(f"- {book.title} by {book.author}")
                book_title = input("\n\nEnter the title of the book you want to borrow: ")
                book_to_borrow = next((b for b in available_books if b.title.lower() == book_title.lower()), None)
                if book_to_borrow:
                    member.borrow_book(book_to_borrow)
                else:
                    print("Book not found or already borrowed.")
            else:
                print("No books are currently available.")

        elif choice == '2':
            if member.borrowed_books:
                print("\n\nBelow are the Books You Borrowed:")
                for book in member.borrowed_books:
                    print(f"- {book.title}")
                book_title = input("\n\nEnter the title of the book you want to return: ")
                book_to_return = next((b for b in member.borrowed_books if b.title.lower() == book_title.lower()), None)
                if book_to_return:
                    member.return_book(book_to_return)
                else:
                    print("You have not borrowed that book.")
            else:
                print("You have no books to return.")

        elif choice == '3':
            member.list_borrowed_books()

        elif choice == '4':
            print("\n\t\t\t\t\tExiting the library system. Goodbye!")
            break

        else:
            print("\nInvalid choice. Please try again.")
# Run the program
main()