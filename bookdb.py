class Book:
    def __init__(self, title, author, isbn, avail):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.avail = avail
        
    def __str__(self):
        return f"'{self.title}' by {self.author} (ISBN: {self.isbn}) Status: {self.avail}"

class BookDB:
    def __init__(self):
        self.books = []
        self.add_defb()

    def add_defb(self):
        defb = [
            Book("1984", "George Orwell", "9780451524935", "Available"),
            Book("To Kill a Mockingbird", "Harper Lee", "9780061120084", "Available"),
            Book("The Great Gatsby", "F. Scott Fitzgerald", "9780743273565", "Borrowed"),
            Book("Moby Dick", "Herman Melville", "9781503280786", "Borrowed"),
            Book("War and Peace", "Leo Tolstoy", "9781420954308", "Available")
        ]
        for book in defb:
            self.books.append(book)
        
    def reg_book(self, book):
        self.books.append(book)
        print(f"Added to database: {book}\n")

    def search_book(self, search_term):
        found_books = [
            book for book in self.books if
            (search_term.lower() in book.title.lower()  or
             search_term.lower() in book.author.lower() or
             search_term == book.isbn)
        ]

        if found_books:
            print("Search Results: ")
            for book in found_books:
                print(book)
            print()
        else:
            print("No books found matching the search term.\n")

    def borrow_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                if book.avail == "Available":
                    book.avail = "Borrowed"
                    print(f"Book '{book.title}' is borrowed for one (1) month.\n")
                    return
                else:
                    print(f"Book '{book.title}' is already borrowed.\n")
                    return
        print("Book not found.\n")


    def return_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                if book.avail == "Borrowed":
                    book.avail = "Available"
                    print(f"Book is returned to database.\n")
                    return
                else:
                    print("Book is already available. Are you sure you take it from this database?\n")
                    return
        print("Book is not listed in the database. Are you sure you borrowed this book?\n")
    
    def list_books(self):
        if not self.books:
            print("No books found in the database.\n")
        else:
            for book in self.books:
                print(book)
            print()
                
def display_menu():
    print("Welcome to the Book Database v0.1")
    print("="*35)
    print("1. Search a book in the database")
    print("2. Display all books in the database")
    print("3. Register a book to the database")
    print("4. Borrow a book")
    print("5. Return a book")
    print("6. Exit")
    print("="*35)

def main():
    db = BookDB()
    while True:
        display_menu()
        opt = input("Enter a number between [1,6]: ")

        if opt == "1":
            sterm = input("Enter the title, author name or isbn number of the book: ")
            db.search_book(sterm)
        elif opt == "2":
            db.list_books()
        elif opt == "3":
            title = input("Enter the book title: ")
            author = input("Enter the author name: ")
            isbn = input("Enter the ISBN number: ")
            avail = "Available"
            nb = Book(title, author, isbn, avail)
            db.reg_book(nb)
        elif opt == "4":
            btitle = input("Enter the book title you want to borrow: ")
            db.borrow_book(btitle)
        elif opt == "5":
            rtitle = input("Enter the book title you want to return: ")
            db.return_book(rtitle)
        elif opt == "6":
            print("Quitting...")
            exit()
        else:
            print("Enter a valid number between [1,6]")
            
            
if __name__ == "__main__":
    main()
