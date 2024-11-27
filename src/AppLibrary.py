import requests
from repositories import book_repository, article_repository, inproceedings_repository
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

    def create_article(self, key, author, title, year, journal):
        data = {
            "key": key,
            "author": author,
            "title": title,
            "publisher": year,
            "journal": journal
        }

        requests.post(f"{self._base_url}/new_article.html", data=data)

    def create_inproceedings(self, key, author, title, year, booktitle):
        data = {
            "key": key,
            "author": author,
            "title": title,
            "publisher": year,
            "booktitle": booktitle
        }

        requests.post(f"{self._base_url}/new_inproceedings.html", data=data)

    def get_books(self):
        with app.app_context():
            books = book_repository.get_books()
            return str(books)
        
    def get_articles(self):
        with app.app_context():
            articles = article_repository.get_articles()
            return str(articles)
        
    def get_inproceedings(self):
        with app.app_context():
            indproceedings = inproceedings_repository.get_inproceedings()
            return str(indproceedings)
        
    def should_be_equal(self, str1, str2):
        return str1 == str2