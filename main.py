class Library:
    # class variable
    books = []
    # constructor
    def __init__(self, bookList):
        self.books = bookList
    # display books
    def display(self):
        for i in self.books:
            print(i)

    # borrow book
    def borrow(self, book):
        if book in self.books:
            self.books.remove(book)
            print("You have borrowed a book")
        else:
            print("The book is not available")

# Main
bookList = ["The Journey Of Mary", "The Adventures of Toto", "The private zoo of Grandfather", "Happy Prince"]
# Create object
library = Library(bookList)

while True:
    print("/--- Library menu ---")
    print("1. Display Menu")
    print("2. Borrow a book")
    print("3. Return a book")
    print("4. Exit")
    choice = input("Enter the number [1/2/3/4]:")

    if choice =="1":
       library.display()
    elif choice == "2":
        book = input('Enter the book you want to borrow:')
        library.borrow(book)
    elif choice == "4":
        break
    else:
        print('Please choose a valid option')

    