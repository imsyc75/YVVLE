from config import db
from sqlalchemy import text

from entities.article import Article
from util import validate

def get_articles():
    result = db.session.execute(text("SELECT id, key, author, title, year, journal FROM articles"))
    articles = result.fetchall()
    #Return an array of article objects
    return [Article(article[0], article[1], article[2], article[3], article[4], article[5]) for article in articles] 

def create_article(key, author, title, year, journal):
    validate([key, author, title, year, journal])

    sql = text("INSERT INTO articles (key, author, title, year, journal) VALUES (:key, :author, :title, :year, :journal)")
    db.session.execute(sql, { "key":key, "author":author, "title":title, "year":year, "journal":journal })
    db.session.commit()

def delete_article(key):
    sql = text("DELETE FROM articles WHERE key=:key")
    db.session.execute(sql, { "key":key })
    db.session.commit()    
    print("Deleted article " + key)   
