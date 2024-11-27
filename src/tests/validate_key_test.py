import unittest
from AppLibrary import AppLibrary
from db_helper import reset_db
from repositories import book_repository, article_repository, inproceedings_repository
from config import app

class TestKeyValidation(unittest.TestCase):
    def setUp(self):
        reset_db()

    def test_book_with_same_key_isnt_inserted_into_db(self):
        # Test with a book
        with app.app_context():
            # Adding a book reference with the key: "ABC"
            self.applib = AppLibrary()
            self.applib.create_book("ABC", "kalle", "kallen kirja", "1999", "SKS")

            # Create another book with the same key
            self.applib.create_book("ABC", "sami", "samin kirja", "1998", "Karisto")
            books_in_db = self.applib.get_books()
            print(books_in_db)

        # Check that there is only one book in the database
        self.assertEqual(1, len(books_in_db))

    # def test_article_with_same_key_isnt_inserted_into_db(self):
    #     # Test with a book
    #     with app.app_context():
    #         # Adding an article reference with the key: "ABC"
    #         self.applib = AppLibrary()
    #         self.applib.create_article("DSA", "kalle", "kallen artikkeli", "1999", "lehti")

    #         # Create another article with the same key
    #         self.applib.create_article("ABC", "sami", "samin artikkeli", "1998", "lehti")
    #         articles_in_db = article_repository.get_articles()

    #     # Check that there is only one book in the database
    #     self.assertEqual(1, len(articles_in_db))
    
    # def test_indproceedings_with_same_key_isnt_inserted_into_db(self):
    #     # Test with a book
    #     with app.app_context():
    #         # Adding an inproceedings reference with the key: "ABC"
    #         self.applib = AppLibrary()
    #         self.applib.create_inproceedings("ABC", "kalle", "kallen kirja", "1999", "SKS")

    #         # Create another inproceeding with the same key
    #         self.applib.create_inproceedings("ABC", "sami", "samin kirja", "1998", "Karisto")
    #         inproceedings_in_db = inproceedings_repository.get_inproceedings()

    #     # Check that there is only one book in the database
    #     self.assertEqual(1, len(inproceedings_in_db))