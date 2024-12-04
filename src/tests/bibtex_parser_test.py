import unittest
from entities.book import Book
from entities.article import Article
from entities.inproceedings import Inproceedings
from bibtex_parser import parse_article, parse_book, parse_inproceedings

class TestBibTexParser(unittest.TestCase):
    def test_parse_book(self):
        book = Book(1, "kirja123", "kalle", "kallen kirja", "1999", "SKS")
        expected = f"""@book{'{'}kirja123,
    author = {'{'}kalle{'}'},
    title = {'{'}kallen kirja{'}'},
    year = {'{'}1999{'}'},
    publisher = {'{'}SKS{'}'}
{'}'}"""
        
        self.assertEqual(expected, parse_book(book))

    def test_parse_article(self):
        article = Article(1, "artikkeli123", "kalle", "kallen artikkeli", "1999", "lehti")
        expected = f"""@article{'{'}artikkeli123,
    author = {'{'}kalle{'}'},
    title = {'{'}kallen artikkeli{'}'},
    year = {'{'}1999{'}'},
    journal = {'{'}lehti{'}'}
{'}'}"""
        
        self.assertEqual(expected, parse_article(article))

    def test_parse_inproceedings(self):
        inproceedings = Inproceedings(1, "inproceedings123", "kalle", "kallen inproceedings", "1999", "kirja")
        expected = f"""@inproceedings{'{'}inproceedings123,
    author = {'{'}kalle{'}'},
    title = {'{'}kallen inproceedings{'}'},
    year = {'{'}1999{'}'},
    booktitle = {'{'}kirja{'}'}
{'}'}"""
        
        self.assertEqual(expected, parse_inproceedings(inproceedings))