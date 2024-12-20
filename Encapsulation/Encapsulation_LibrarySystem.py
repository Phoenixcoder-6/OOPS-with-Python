class LibraryBook:
    def __init__(self,title,author, available_copies):
        self.__title= title
        self.__author= author
        self.__available_copies= available_copies

    def get_title(self):
        return self.__title
    def get_author(self):
        return self.__author
    def get_available_copies(self):
        return self.__available_copies
    
    def set_available_copies(self, number):
        if number>=0:
            self.__available_copies=number
        else:
            print("Books not available!!")
    
    def borrow_book(self):
        if self.__available_copies>0:
            self.__available_copies-=1
            print("Book borrowed successfully.")
        else:
            print("No books to borrow")
    def return_book(self):
        self.__available_copies += 1
        print("Book returned successfully.")


# Testing the class
book = LibraryBook("1984", "George Orwell", 3)
print(f"Title: {book.get_title()}")
print(f"Author: {book.get_author()}")
print(f"Available Copies: {book.get_available_copies()}")

book.borrow_book()
print(f"Available Copies after borrowing: {book.get_available_copies()}")

book.return_book()
print(f"Available Copies after returning: {book.get_available_copies()}")

    

    