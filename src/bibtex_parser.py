
from repositories.book_repository import get_books, Book
from repositories.article_repository import get_articles, Article
from repositories.inproceedings_repository import get_inproceedings, Inproceedings

# Keys should be unique!

# Parsing assumes there are all of the expected parameters

def parse_to_file():
    output = ''

    books = get_books()
    articles = get_articles()
    inprocs = get_inproceedings()

    for book in books:
        output += parse_book(book) + "\n\n"
    
    for article in articles:
        output += parse_article(article) + "\n\n"

    for inpro in inprocs:
        output += parse_inproceedings(inpro) + "\n\n"

    with open("references.bib", "w") as file:
        file.write(output)

def parse_books_to_list():
    output = []

    books = get_books()

    for book in books:
        output.append(parse_book(book))

    return output

def parse_articles_to_list():
    output = []

    articles = get_articles()

    for article in articles:
        output.append(parse_article(article))

    return output

def parse_inproceedings_to_list():
    output = []

    inprocs = get_inproceedings()

    for inproc in inprocs:
        output.append(parse_inproceedings(inproc))

    return output

def parse_book(book : Book):
    return f"""@book{'{'}{book.key},
    author = {'{' + book.author + '}'},
    title = {'{' + book.title + '}'},
    year = {'{' + book.year + '}'},
    publisher = {'{' + book.publisher + '}'}
{'}'}"""

def parse_article(article : Article):
    return f"""@article{'{'}{article.key},
    author = {'{' + article.author + '}'},
    title = {'{' + article.title + '}'},
    year = {'{' + article.year + '}'},
    journal = {'{' + article.journal + '}'}
{'}'}"""

def parse_inproceedings(inpro : Inproceedings):
    return f"""@inproceedings{'{'}{inpro.key},
    author = {'{' + inpro.author + '}'},
    title = {'{' + inpro.title + '}'},
    year = {'{' + inpro.year + '}'},
    booktitle = {'{' + inpro.booktitle + '}'}
{'}'}"""