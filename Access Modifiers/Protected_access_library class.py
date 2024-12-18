class Library:
    def __init__(self):
        self._books=[]

    def addbook(self,title):
        self._books.append(title)
        print(f"{title} book added")
    
    def showbooks(self):
        if self._books:
            print("The books are:\n")
            for book in self._books:
                print(f"-{book}")

        else:
            print("No books to show.")

class Community_library(Library):
    def display_book_count(self):
        print(f" The number of the books available: {len(self._books)}")


# Create an instance of the CommunityLibrary class
community_library = Community_library()

# Adding books to the library
community_library.addbook("The Alchemist")
community_library.addbook("1984")
community_library.addbook("To Kill a Mockingbird")

# Displaying all books
community_library.showbooks()

# Displaying the total number of books (accessing the protected attribute)
community_library.display_book_count()