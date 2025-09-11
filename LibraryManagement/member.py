class Member:
    MAX_BORROW=3
    def __init__(self,name,member_id):
        self.name=name
        self.member_id=member_id
        self.borrowed_books=[]

    def borrow_book(self, book):
        if len(self.borrowed_books) >= self.MAX_BORROW:
            print(f"{self.name} cannot borrow more than {self.MAX_BORROW} books.")
            return
        if book.borrow():
            self.borrowed_books.append(book)
            print(f"{self.name} borrowed '{book.title}'.")
        else:
            print(f"Book '{book.title}' is currently not available.")

    def return_books(self,book):
        if book in self.borrowed_books:
            book.return_book()
            self.borrowed_books.remove(book)
            print(f"{self.name} returned '{book.title}'.")

    def display_books(self):
        print(f"{self.name}'s borrowed books:")
        for book in self.borrowed_books:
            print(f"-{book.title}")