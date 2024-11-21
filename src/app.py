from flask import redirect, render_template, request, jsonify, flash
from db_helper import reset_db

#Get stuff from book_repository
from repositories.book_repository import get_books, create_book
from config import app, test_env
from util import validateNotEmpty

@app.route("/")
def index():
    return render_template("index.html") 

@app.route("/new_book")
def new():
    return render_template("new_book.html")

#Create new book
@app.route("/create_book", methods=["POST"])
def book_creation():
    key = request.form.get("key")
    author = request.form.get("author")
    title = request.form.get("title")
    year = request.form.get("year")
    publisher = request.form.get("publisher")

    #Validate that parameters are not empty, if they are an exception is thrown
    try: 
        validateNotEmpty([key, author, title, year, publisher])
        create_book(key, author, title, year, publisher)
        return redirect("/")
    except Exception as error:
        #Print the error and put it in a flask flash
        print(str(error))
        flash(str(error))
        return  redirect("/new_book")

#Create new article
@app.route("/create_article", methods=["POST"])
def article_creation():
    key = request.form.get("key")
    author = request.form.get("author")
    title = request.form.get("title")
    year = request.form.get("year")
    journal = request.form.get("journal")

    #Validate that parameters are not empty, if they are an exception is thrown
    try: 
        validateNotEmpty([key, author, title, year, journal])
        create_article(key, author, title, year, journal)
        return redirect("/")
    except Exception as error:
        #Print the error and put it in a flask flash
        print(str(error))
        flash(str(error))
        return  redirect("/new_journal")

#Create new inproceeding
@app.route("/create_inproceeding", methods=["POST"])
def inproceeding_creation():
    key = request.form.get("key")
    author = request.form.get("author")
    title = request.form.get("title")
    year = request.form.get("year")
    booktitle = request.form.get("booktitle")

    #Validate that parameters are not empty, if they are an exception is thrown
    try: 
        validateNotEmpty([key, author, title, year, booktitle])
        create_inproceeding(key, author, title, year, booktitle)
        return redirect("/")
    except Exception as error:
        #Print the error and put it in a flask flash
        print(str(error))
        flash(str(error))
        return  redirect("/new_inproceeding")



# this will clear the database but not drop tables
if test_env:
    @app.route("/reset_db")
    def reset_database():
        reset_db()
        return jsonify({ 'message': "db reset" })
