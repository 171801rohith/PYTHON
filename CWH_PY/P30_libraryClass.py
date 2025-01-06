# Write a Library class with no_of_books and books as two instance variables. 
# Write a program to create a library from this Library class and show how you can print all books, add a book and get the number of books using different methods. 
# Show that your program doesnt persist the books after the program is stopped!

class Library:
    books = []
    no_of_books = 0

    def addbook(self, book_name):
        self.books.append(book_name)
        self.no_of_books += 1

    def displayBooks(self):
        if len(self.books) == self.no_of_books:
            return self.books
        elif self.no_of_books == 0:
            return "No books were added"
        else:
            return "Some error occurred"
    

lib = Library()
lib.addbook("Hello, JAVA!")
lib.addbook("Python Goes Wild")
print("Books:", lib.displayBooks())

