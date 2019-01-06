# -*- coding: utf-8 -*-

from sqlalchemy_seed import (
    create_table,
    drop_table,
    load_fixtures,
    load_fixture_files,
)
from seedModel import Base, session

import os,sys,inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir) 
from models.AuthorModel import Author
from models.BookModel import Book


def main():
    path = './'
    fixtures = load_fixture_files(path, ['AuthorsData.yaml', 'BookData.yaml'])
    load_fixtures(session, fixtures)


if __name__ == '__main__':
    main()