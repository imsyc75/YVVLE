from config import db
from sqlalchemy import text

from entities.book import Book
from util import validate

def get_books():
    result = db.session.execute(text("SELECT id, key, author, title, year, publisher FROM books"))
    books = result.fetchall()
    #Return an array of book objects
    return [Book(book[0], book[1], book[2], book[3], book[4], book[5]) for book in books] 

def create_book(key, author, title, year, publisher):
    validate([key, author, title, year, publisher])

    sql = text("INSERT INTO books (key, author, title, year, publisher) VALUES (:key, :author, :title, :year, :publisher)")
    db.session.execute(sql, { "key":key, "author":author, "title":title, "year":year, "publisher":publisher })
    db.session.commit()

def delete_book(key):
    sql = text("DELETE FROM books WHERE key=:key")
    db.session.execute(sql, { "key":key })
    db.session.commit()    
    print("Deleted book " + key)
