from config import db
from sqlalchemy import text
from db_helper import table_names
from util import *

def get_all_keys():
    command = ''
    for i in range(len(table_names)):
        command += f"SELECT key FROM {table_names[i]}"
        if (i != len(table_names) - 1):
            command += " UNION ALL "
    command += ";"
    
    result = db.session.execute(text(command))
    keys = result.fetchall()
    return [key[0] for key in keys]
