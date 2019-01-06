from flask import Flask
from app import db
import json

class Book(db.Model):
    __tablename__ = "books"

    # Columns
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(120), nullable=False)
    price = db.Column(db.Float, nullable=False)
    isbn = db.Column(db.Integer, unique=True)
    authors_id = db.Column(db.Integer, db.ForeignKey('authors.id'), nullable=True)

    # Use to return data in json format
    def json(self):
        return {"name": self.name, "price": self.price, "isbn": self.isbn, "authors_id": self.authors_id}

    def add(_name, _price, _isbn):
        result = Book(name=_name, price=_price, isbn=_isbn)
        db.session.add(result)
        db.session.commit()
        return Book.json(result)

    def add_book(data):
        result = Book(name=data['name'], price=data['price'], isbn=data['isbn'])
        db.session.add(result)
        db.session.commit()
        return Book.json(result)
    
    def get_all():
        return [Book.json(book) for book in db.session.query(Book)]

    def getByIsbn(_isbn):
        return Book.json(Book.query.filter_by(isbn=_isbn).first())

    def deleteByIsbn(_isbn):
        book = Book.query.filter_by(isbn=_isbn).delete()
        db.session.commit()

    def updateBook(existing_book, meta):
        for key, value in meta.items():
            if key == "name":
                existing_book.name = value
            if key == "price":
                existing_book.price = value
        db.session.commit()

    # Use just when we're in terminal
    def __repr__(self):
        obj = {
            "name": self.name,
            "price": self.price,
            "isbn": self.isbn,
            "authors_id": self.authors_id,
            "id": self.id
        }
        return json.dumps(obj)