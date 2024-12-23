from sqlalchemy import text
from config import db, app


table_names = ["articles", "books", "inproceedings"]


def table_exists(name):
    sql_table_existence = text(
        "SELECT EXISTS ("
        "  SELECT 1"
        "  FROM information_schema.tables"
        f" WHERE table_name = '{name}'"
        ")"
    )

    print(f"Checking if table {name} exists")
    print(sql_table_existence)

    result = db.session.execute(sql_table_existence)
    return result.fetchall()[0][0]

# Resets the db without dropping tables


def reset_db():
    for table_name in table_names:
        print(f"Clearing contents from table {table_name}")
        sql = text(f"DELETE FROM {table_name}")
        db.session.execute(sql)
        db.session.commit()

# Debug function to return the contents of the db

def print_db():
    result = []
    for table_name in table_names:
        result.append(table_name + ":")
        sql = text(f"SELECT * FROM {table_name}")
        result.append(db.session.execute(sql).fetchall())
    return result


def setup_db():
    for table_name in table_names:
        if table_exists(table_name):
            print(f"Table {table_name} exists, dropping")
            sql = text(f"DROP TABLE {table_name}")
            db.session.execute(sql)
            db.session.commit()

        print(f"Creating table {table_name}")

        if table_name == "inproceedings":
            sql = text(
                "CREATE TABLE inproceedings ("
                "  id SERIAL PRIMARY KEY, "
                "  key TEXT NOT NULL,"
                "  author TEXT NOT NULL,"
                "  title TEXT NOT NULL,"
                "  year TEXT NOT NULL,"
                "  booktitle TEXT NOT NULL"
                ")"
            )
        elif table_name == "articles":
            sql = text(
                "CREATE TABLE articles ("
                "  id SERIAL PRIMARY KEY, "
                "  key TEXT NOT NULL,"
                "  author TEXT NOT NULL,"
                "  title TEXT NOT NULL,"
                "  year TEXT NOT NULL,"
                "  journal TEXT NOT NULL"
                ")"
            )
        elif table_name == "books":
            sql = text(
                "CREATE TABLE books ("
                "  id SERIAL PRIMARY KEY, "
                "  key TEXT NOT NULL,"
                "  author TEXT NOT NULL,"
                "  title TEXT NOT NULL,"
                "  year TEXT NOT NULL,"
                "  publisher TEXT NOT NULL"
                ")"
            )
        db.session.execute(sql)
        db.session.commit()


if __name__ == "__main__":
    with app.app_context():
        setup_db()
