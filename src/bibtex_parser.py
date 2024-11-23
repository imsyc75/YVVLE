
from repositories.book_repository import get_books, Book
from repositories.article_repository import get_articles, Article
from repositories.inproceedings_repository import get_inproceedings, Inproceedings

# Keys should be unique!

# Parses the references into a bibtex file called 'references.bib'

# Parsing assumes there are all of the expected parameters

def parse():
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