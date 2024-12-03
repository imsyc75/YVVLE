import random
import requests
from flask import redirect, render_template, request, jsonify, flash, send_file
from db_helper import reset_db, print_db

from repositories.book_repository import get_books, create_book, delete_book
from repositories.inproceedings_repository import get_inproceedings, create_inproceedings, delete_inproceedings
from repositories.article_repository import get_articles, create_article, delete_article
from config import app, test_env

import bibtex_parser
import doi_importer


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/view_books")
def view_books():
    try:
        books = get_books()
        parsed_books = bibtex_parser.parse_books_to_list()

        books_tuple = []
        for i in range(len(books)):
            lines = parsed_books[i].split('\n')
            books_tuple.append(
                (books[i], lines[0], lines[1:(len(lines) - 1)], lines[-1]))

        return render_template("view_books.html", books=books_tuple)
    except Exception as error:
        print(str(error))
        flash(str(error))
        return redirect("/")


@app.route("/view_articles")
def view_articles():
    try:
        articles = get_articles()
        parsed_articles = bibtex_parser.parse_articles_to_list()

        articles_tuple = []
        for i in range(len(articles)):
            lines = parsed_articles[i].split('\n')
            articles_tuple.append(
                (articles[i], lines[0], lines[1:(len(lines) - 1)], lines[-1]))

        return render_template("view_articles.html", articles=articles_tuple)
    except Exception as error:
        print(str(error))
        flash(str(error))
        return redirect("/")


@app.route("/view_inproceedings")
def view_inproceedings():
    try:
        inproceedings = get_inproceedings()
        parsed_inprocs = bibtex_parser.parse_inproceedings_to_list()

        inprocs_tuple = []
        for i in range(len(inproceedings)):
            lines = parsed_inprocs[i].split('\n')
            inprocs_tuple.append(
                (inproceedings[i], lines[0], lines[1:(len(lines) - 1)], lines[-1]))

        return render_template("view_inproceedings.html", inproceedings=inprocs_tuple)
    except Exception as error:
        print(str(error))
        flash(str(error))
        return redirect("/")


@app.route("/new_book")
def new():
    return render_template("new_book.html")


@app.route("/new_article")
def new_article():
    return render_template("new_article.html")


@app.route("/new_inproceedings")
def new_inproceedings():
    return render_template("new_inproceedings.html")


@app.route("/create_book", methods=["POST"])
def book_creation():
    key = request.form.get("key")
    author = request.form.get("author")
    title = request.form.get("title")
    year = request.form.get("year")
    publisher = request.form.get("publisher")

    try: 
        create_book(key, author, title, year, publisher)
        return redirect("/")

    except Exception as error:
        print(str(error))
        flash(str(error))
        return redirect("/new_book")


@app.route("/create_article", methods=["POST"])
def article_creation():
    key = request.form.get("key")
    author = request.form.get("author")
    title = request.form.get("title")
    year = request.form.get("year")
    journal = request.form.get("journal")

    try: 
        create_article(key, author, title, year, journal)
        return redirect("/")

    except Exception as error:
        print(str(error))
        flash(str(error))
        return redirect("/new_article")


@app.route("/create_inproceedings", methods=["POST"])
def inproceedings_creation():
    key = request.form.get("key")
    author = request.form.get("author")
    title = request.form.get("title")
    year = request.form.get("year")
    booktitle = request.form.get("booktitle")

    try: 
        create_inproceedings(key, author, title, year, booktitle)
        return redirect("/")
    except Exception as error:
        print(str(error))
        flash(str(error))
        return redirect("/new_inproceedings")


@app.route('/download')
def download():
    bibtex_parser.parse_to_file()
    path = 'downloadables/references.bib'
    return send_file(path, as_attachment=True)


@app.route("/delete_reference")
def delete_reference():
    books = get_books()
    articles = get_articles()
    inproceedings = get_inproceedings()
    books_tuple = []
    for i in range(len(books)):
        books_tuple.append(books[i])
    inprocs_tuple = []
    for i in range(len(inproceedings)):
        inprocs_tuple.append(inproceedings[i])
    articles_tuple = []
    for i in range(len(articles)):
        articles_tuple.append(articles[i])

    return render_template("delete_reference.html", books=books_tuple,
                           articles=articles_tuple, inproceedings=inprocs_tuple)


@app.route("/del_references", methods=["POST"])
def del_references():
    books = request.form.getlist("books")
    articles = request.form.getlist("articles")
    inproceedings = request.form.getlist("inproceedings")

    try:
        for book in books:
            delete_book(book)
        for article in articles:
            delete_article(article)
        for inproceeding in inproceedings:
            delete_inproceedings(inproceeding)

    except Exception as error:
        print(str(error))
        flash(str(error))

    return redirect("/delete_reference")


@app.route("/doi")
def doi():
    return render_template("doi.html")


@app.route("/upload_doi", methods=['POST'])
def process_doi():
    link = request.form.get("doi")

    try:
        data = doi_importer.convert_doi(link)
        return render_template("review_doi.html", data=data)
    except Exception as error:
        print(str(error))
        flash(str(error))
        return redirect("/doi")


@app.route("/add_doi", methods=['POST'])
def add_doi():
    type = request.form.get("type")
    key = request.form.get("key")

    try:
        if (type == 'article'):
            author = request.form.get("author")
            title = request.form.get("title")
            year = request.form.get("year")
            journal = request.form.get("journal")
            create_article(key, author, title, year, journal)
        
        return redirect("/")
    except Exception as error:
        print(str(error))
        flash(str(error))
        return redirect("/doi")
    
@app.route("/edit_book/<key>")
def edit_book(key):
    try:
        books = get_books()
        for book in books:
            if book.key == key: 
                return render_template("edit_book.html", book=book)
        flash("Book not found")
        return redirect("/view_books")
    except Exception as error:
        print(str(error))
        flash(str(error))
        return redirect("/view_books")

@app.route("/edit_article/<key>")
def edit_article(key):
    try:
        articles = get_articles()
        for article in articles:
            if article.key == key:
                return render_template("edit_article.html", article=article)
        flash("Article not found")
        return redirect("/view_articles")
    except Exception as error:
        print(str(error))
        flash(str(error))
        return redirect("/view_articles")

@app.route("/edit_inproceedings/<key>")
def edit_inproceedings(key):
    try:
        inproceedings = get_inproceedings()
        for inproc in inproceedings:
            if inproc.key == key:
                return render_template("edit_inproceedings.html", inproceedings=inproc)
        flash("Inproceedings not found")
        return redirect("/view_inproceedings")
    except Exception as error:
        print(str(error))
        flash(str(error))
        return redirect("/view_inproceedings")

@app.route("/update_book", methods=["POST"])
def update_book():
    old_key = request.form.get("old_key")
    key = request.form.get("key")
    author = request.form.get("author")
    title = request.form.get("title")
    year = request.form.get("year")
    publisher = request.form.get("publisher")

    try:
        # First delete the old reference
        delete_book(old_key)
        # Then create a new one with updated information
        create_book(key, author, title, year, publisher)
        return redirect("/view_books")
    except Exception as error:
        print(str(error))
        flash(str(error))
        return redirect(f"/edit_book/{old_key}")

@app.route("/update_article", methods=["POST"])
def update_article():
    old_key = request.form.get("old_key")
    key = request.form.get("key")
    author = request.form.get("author")
    title = request.form.get("title")
    year = request.form.get("year")
    journal = request.form.get("journal")

    try:
        delete_article(old_key)
        create_article(key, author, title, year, journal)
        return redirect("/view_articles")
    except Exception as error:
        print(str(error))
        flash(str(error))
        return redirect(f"/edit_article/{old_key}")

@app.route("/update_inproceedings", methods=["POST"])
def update_inproceedings():
    old_key = request.form.get("old_key")
    key = request.form.get("key")
    author = request.form.get("author")
    title = request.form.get("title")
    year = request.form.get("year")
    booktitle = request.form.get("booktitle")

    try:
        delete_inproceedings(old_key)
        create_inproceedings(key, author, title, year, booktitle)
        return redirect("/view_inproceedings")
    except Exception as error:
        print(str(error))
        flash(str(error))
        return redirect(f"/edit_inproceedings/{old_key}")


# Useful debug functions
# TEST_ENV=true in .env
if test_env:
    # this will clear the database but not drop tables
    @app.route("/reset_db")
    def reset_database():
        reset_db()
        flash("DB RESET")
        return redirect("/")

    # This will print the content of the database TODO in proper json format
    @app.route("/print_db")
    def print_database():
        results = print_db()
        return jsonify(str(results))

    # This will fill the database with random stuff using words from the 5000 word dictionary.
    # E.g. 127.0.0.1:5001/fill_db=99 will create 33 books, 33 articles and 33 inproceedings
    @app.route("/fill_db=<item_amount>")
    def fill_database(item_amount):
        word_site = "https://raw.githubusercontent.com/MichaelWehar/Public-Domain-Word-Lists/master/5000-more-common.txt"

        response = requests.get(word_site, verify=True, timeout=10)
        words = response.text.splitlines()

        for i in range(int(item_amount)):
            try:
                if i % 3 == 0:
                    create_book(words[i*4], words[i*4+1], words[i*4+2],
                                str(random.randint(1, 2024)), words[i*4+3])
                elif i % 3 == 1:
                    create_article(
                        words[i*4], words[i*4+1], words[i*4+2], str(random.randint(1, 2024)), words[i*4+3])
                elif i % 3 == 2:
                    create_inproceedings(
                        words[i*4], words[i*4+1], words[i*4+2], str(random.randint(1, 2024)), words[i*4+3])
            except Exception as error:
                print(str(error))
                flash(str(error))

        return redirect("/")
