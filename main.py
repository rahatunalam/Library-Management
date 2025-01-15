class Book:
    def __init__(self,title,author,genre,is_borrowed):
        self.title = title
        self.author = author
        self.genre = genre
        self.is_borrowed = is_borrowed
    def borrow_book(self):
        print("Book Title: "+self.title)
        print("Book author: "+self.author)
        print("Book genre: "+self.genre)
        print("Borrowed book: "+self.is_borrowed)

    def return_book(self):
        print("Book Title: " + self.title)
        print("Book author: " + self.author)
        print("Book genre: " + self.genre)
        #print("Borrowed book: " + self.is_borrowed)

class Borrower:
     def __init__(self,name,borrower_books,history):
         self.name =name
         self.borrower_books= borrower_books
         self.history= history

     def borrow(self,book):
        print()

     def retun_book(self,book):
            print()
class Library:
    def __init__(self,books,borrowers):
        self.books=books
        self.borrowers=borrowers

    def add_book(self,book):
        book_list.append(book)
        print(book_list)
    def remove_book(self,book):
        book_list.remove(book)
        print(book_list)
    def list_available_book(self,books):
        print(book_list)
    def list_generes(self):
        print()
    def find_borrower(self,name):
        borrower_list.append(name)
        print(borrower_list)

book_list =[]
borrower_list = []
history =[]
a = int(input("How many books :"))
l=Library(book_list,borrower_list)
x=input("Do you want to add Book y/n: ")
if x=="y":
    for _ in range(a):
        b = input("Book name: ")
        l.add_book(b)
y=input("Do you want to remove Book y/n: ")
if x=="y":
    b = input("Book name: ")
    l.remove_book(b)

b = Borrower(borrower_list,book_list,history)

