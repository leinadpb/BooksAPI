from flask_sqlalchemy import SQLAlchemy
from settings import db
from AuthorModel import Author
from BookModel import Book


db.create_all()

