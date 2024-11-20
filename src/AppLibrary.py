import requests
from repositories import book_repository
from config import app

class AppLibrary:
    def __init__(self):
        self._base_url = "http://localhost:5001"
        
    # def reset_application(self):
    #     requests.post()

    def create_book(self, key, author, title, year, publisher):
        data = {
            "key": key,
            "author": author,
            "title": title,
            "publisher": year,
            "year": publisher
        }

        requests.post(f"{self._base_url}/new_book.html", data=data)

    def get_books(self):
        with app.app_context():
            books = book_repository.get_books()
            return str(books)
        
    def should_be_equal(self, str1, str2):
        return str1 == str2