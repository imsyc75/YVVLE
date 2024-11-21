from config import db
from sqlalchemy import text

from entities.inproceeding import Inproceeding

def get_inproceedings():
    result = db.session.execute(text("SELECT id, key, author, title, year, booktitle FROM inproceedings"))
    inproceedings = result.fetchall()
    #Return an array of inproceeding objects
    return [Inproceeding(inproceeding[0], inproceeding[1], inproceeding[2], inproceeding[3], inproceeding[4], inproceeding[5]) for inproceeding in inproceedings] 

#Insert the values to the database created by db_helper.py
def create_inproceeding(key, author, title, year, booktitle):
    sql = text("INSERT INTO inproceedings (key, author, title, year, booktitle) VALUES (:key, :author, :title, :year, :booktitle)")
    db.session.execute(sql, { "key":key, "author":author, "title":title, "year":year, "booktitle":booktitle })
    db.session.commit()

    
