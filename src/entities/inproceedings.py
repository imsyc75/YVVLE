class Inproceedings:
    def __init__(self, id, key, author, title, year, booktitle):
        self.id = id
        self.key = key
        self.author = author
        self.title = title
        self.year = year
        self.booktitle = booktitle

    def __str__(self):
        return f"{self.key}, {self.author}, {self.title}, {self.year}, {self.booktitle}"
