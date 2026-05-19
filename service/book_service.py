from models.book_models import Book
from extension import db


def create_book(data):
    
    new_book = Book(
        title = data["title"],
        author = data["author"]
    )
    
    db.session.add(new_book)
    db.session.commit()
    
    return new_book


def get_books(page = 1,per_page=5):
    return Book.query.paginate(
        page = page,
        per_page = per_page,
        error_out= False
    )
    
def one_book(id):
    return db.session.get(Book, id)

def up_books(id,data):
    book = one_book(id)
    
    if book is None:
        return None
    
    if book is not None:
        book.title = data.get("title", book.title)
        book.author = data.get("author", book.author)
        book.available = data.get("available", book.available)
        
        db.session.commit()
    
    return book

def supp_books(id):
    book = one_book(id)
    
    if book is not None:
        db.session.delete(book)
        db.session.commit()
        
    return book
    
    
