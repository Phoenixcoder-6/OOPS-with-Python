class Book:
    def __init__(self,title,author,price):
        self.title=title
        self.author=author
        self.price=price

    def show_details(self):
        print(f"{self.title} is written by {self.author} and costs {self.price} Rs.")

book_instance= Book("Geetanjali","Tagore", 1200)
book_instance.show_details()
