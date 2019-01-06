from flask_sqlalchemy import SQLAlchemy
import os
from common.common_imports import *

# print(os.environ['DATABASE_URL'])
# print( current_app.config.get('SQLALCHEMY_DATABASE_URI'))

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.debug = os.environ.get('DEBUG')
db = SQLAlchemy(app)

# Author's import should be removed if you're going to execute database queries in database\
# Just to avoid redundant imports and python doesn't go crazy. ;)
from models.AuthorModel import Author
from models.BookModel import Book

from controllers.authorController import authorController
from controllers.bookController import bookController

authorController(app, Author)
bookController(app, Book)

# GET /  -  Main Route
@app.route('/')
def root():
    return "Go to /books\nOr /authors"

# Run
if __name__ == "__main__":
    app.run(port=os.environ['PORT'])