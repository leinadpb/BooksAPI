from settings import db
from BookModel import Book
from AuthorModel import Author
import pprint
import json

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