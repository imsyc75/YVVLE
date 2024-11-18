from flask import redirect, render_template, request, jsonify, flash
from db_helper import reset_db

#Get stuff from book_repository
from repositories.book_repository import get_books, create_book
from config import app, test_env
from util import validate_book

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
    try:
        #validate_book(content) TODO
        create_book(key, author, title, year, publisher)
        return redirect("/")
    except Exception as error:
        flash(str(error))
        return  redirect("/new_todo")

# testausta varten oleva reitti
if test_env:
    @app.route("/reset_db")
    def reset_database():
        reset_db()
        return jsonify({ 'message': "db reset" })
