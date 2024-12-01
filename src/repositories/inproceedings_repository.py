from config import db
from sqlalchemy import text

from entities.inproceedings import Inproceedings
from util import validate

def get_inproceedings():
    result = db.session.execute(text("SELECT id, key, author, title, year, booktitle FROM inproceedings"))
    inproceedings = result.fetchall()
    #Return an array of inproceedings objects
    return [Inproceedings(inproceeding[0], inproceeding[1], inproceeding[2], inproceeding[3], inproceeding[4], inproceeding[5]) for inproceeding in inproceedings] 

def create_inproceedings(key, author, title, year, booktitle):
    validate([key, author, title, year, booktitle])

    sql = text("INSERT INTO inproceedings (key, author, title, year, booktitle) VALUES (:key, :author, :title, :year, :booktitle)")
    db.session.execute(sql, { "key":key, "author":author, "title":title, "year":year, "booktitle":booktitle })
    db.session.commit()

def delete_inproceedings(key):
    sql = text("DELETE FROM inproceedings WHERE key=:key")
    db.session.execute(sql, { "key":key })
    db.session.commit()    
    print("Deleted inproceedings " + key)      
