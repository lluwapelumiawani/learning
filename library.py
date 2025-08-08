class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_borrowed = False

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title, author, isbn):
        new_book = Book(title, author, isbn)
        self.books.append(new_book)
        print(f'Added book: "{title}" by {author} (ISBN: {isbn})')

    def borrow_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                if not book.is_borrowed:
                    book.is_borrowed = True
                    print(f'You have borrowed "{book.title}"')
                    return
                else:
                    print(f'Sorry, "{book.title}" is already borrowed.')
                    return
        print('Book not found.')

    def return_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                if book.is_borrowed:
                    book.is_borrowed = False
                    print(f'You have returned "{book.title}"')
                    return
                else:
                    print(f'"{book.title}" was not borrowed.')
                    return
        print('Book not found.')

    def list_available_books(self):
        available_books = [book for book in self.books if not book.is_borrowed]
        if available_books:
            print("Available books:")
            for book in available_books:
                print(f'"{book.title}" by {book.author} (ISBN: {book.isbn})')
        else:
            print("No available books.")

if __name__ == "__main__":
    library = Library()

    library.add_book("The Lekki Headmaster", "Kabir Alabi Garba", "09115374909")
    library.add_book("Talking To Strangers", "Malcolm Gladwe", "9780316478526")
    library.add_book("The Lord of the Rings ", "J. R. R. Tolkien", "9780008537807")

    library.list_available_books()

    library.borrow_book("9780008537807")

    library.list_available_books()

    library.return_book("9780008537807")

    library.list_available_books()