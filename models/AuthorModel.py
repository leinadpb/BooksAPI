from flask import Flask
from app import db
import json

class Author(db.Model):
    __tablename__ = "authors"

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    lastname = db.Column(db.String(20), nullable=False)
    books = db.relationship('Book', backref='author', lazy=True)

    def json(self):
        return { "name": self.name, "lastname": self.lastname, "books": self.books }

    def add(_name, _lastname):
        result = Author(name=_name, lastname=_lastname)
        db.session.add(result)
        db.session.commit()
        return Author.json(result)
    
    def add_author(_author):
        result = Author(name=_author["name"], lastname=_author["lastname"])
        db.session.add(result)
        db.session.commit()
        return Author.json(result)

    def __repr__(self):
        obj = {
            "name": self.name,
            "lastname": self.lastname,
            "books": self.books,
            "id": self.id
        }
        return json.dumps(obj)



