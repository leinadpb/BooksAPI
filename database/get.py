import pprint
import json

import os,sys,inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir) 
from models.AuthorModel import Author 
from models.BookModel import Book

# VERIFY AUTHOR MODEL IS NOT BEING IMPORTED IN > booksapi/app.py

pp = pprint.PrettyPrinter(indent=2)

def getAllBooks():
    pp.pprint(Book.query.all())

def getAllAuthors():
    pp.pprint(Author.query.all())

def main():
    print('Books')
    getAllBooks()
    print('Authors')
    getAllAuthors()

if __name__ == '__main__':
    main()