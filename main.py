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
    elif choice == "4":
        break
    else:
        print('Please choose a valid option')

    