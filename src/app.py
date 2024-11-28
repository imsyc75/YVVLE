from flask import redirect, render_template, request, jsonify, flash, json, send_file
from db_helper import reset_db, print_db

from repositories.book_repository import *
from repositories.inproceedings_repository import *
from repositories.article_repository import *
from config import app, test_env
from util import validate_not_empty, validate_length, validate_key

import bibtex_parser

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
            books_tuple.append((books[i], lines[0], lines[1:(len(lines) - 1)], lines[-1]))

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
            articles_tuple.append((articles[i], lines[0], lines[1:(len(lines) - 1)], lines[-1]))

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
            inprocs_tuple.append((inproceedings[i], lines[0], lines[1:(len(lines) - 1)], lines[-1]))

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
        validate_not_empty([key, author, title, year, publisher])
        validate_length([key, author, title, year, publisher], 1, 255)
        validate_key(key, get_book_keys() + get_article_keys() + get_inproceedings_keys())
        create_book(key, author, title, year, publisher)
        return redirect("/")
        
    except Exception as error:
        print(str(error))
        flash(str(error))
        return  redirect("/new_book")

@app.route("/create_article", methods=["POST"])
def article_creation():
    key = request.form.get("key")
    author = request.form.get("author")
    title = request.form.get("title")
    year = request.form.get("year")
    journal = request.form.get("journal")

    try: 
        validate_not_empty([key, author, title, year, journal])
        validate_length([key, author, title, year, journal], 1, 255)
        validate_key(key, get_book_keys() + get_article_keys() + get_inproceedings_keys())
        create_article(key, author, title, year, journal)
        return redirect("/")

    except Exception as error:
        print(str(error))
        flash(str(error))
        return  redirect("/new_article")

@app.route("/create_inproceedings", methods=["POST"])
def inproceedings_creation():
    key = request.form.get("key")
    author = request.form.get("author")
    title = request.form.get("title")
    year = request.form.get("year")
    booktitle = request.form.get("booktitle")

    try: 
        validate_not_empty([key, author, title, year, booktitle])
        validate_length([key, author, title, year, booktitle], 1, 255)
        validate_key(key, get_book_keys() + get_article_keys() + get_inproceedings_keys())
        create_inproceedings(key, author, title, year, booktitle)
        return redirect("/")
    except Exception as error:
        print(str(error))
        flash(str(error))
        return  redirect("/new_inproceedings")

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

    return render_template("delete_reference.html", books=books_tuple, articles=articles_tuple, inproceedings=inprocs_tuple)



#Useful debug functions
#TEST_ENV=true in .env
if test_env:
    # this will clear the database but not drop tables
    @app.route("/reset_db")
    def reset_database():
        reset_db()
        return jsonify({ 'message': "db reset" })

    #This will print the content of the database TODO in proper json format
    @app.route("/print_db")
    def print_database():
        results = print_db()
        return jsonify(str(results))
