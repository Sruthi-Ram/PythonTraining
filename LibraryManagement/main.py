from Book import BookManagement
from member import Member
book1=BookManagement("Python Basics","Alice","ISBN001")
book2=BookManagement("Learning OOP","Bob","ISBN002")
book3=BookManagement("Data Science 101","Charlie","ISBN003")
for b in [book1,book2,book3]:
    b.display()
member1=Member("Alice",101)
member2=Member("Bob",102)
member1.borrow_book(book1)
member1.borrow_book(book2)
member1.borrow_book(book3)
member2.borrow_book(book1)
member1.display_books()
member2.display_books()
member1.return_books(book2)
member2.borrow_book(book2)