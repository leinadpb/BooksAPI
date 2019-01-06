# -*- coding: utf-8 -*-

from sqlalchemy_seed import (
    create_table,
    drop_table,
    load_fixtures,
    load_fixture_files,
)
from seedModel import Base, session
from AuthorModel import Author
from BookModel import Book


def main():
    path = './'
    fixtures = load_fixture_files(path, ['AuthorsData.yaml', 'BookData.yaml'])
    load_fixtures(session, fixtures)


if __name__ == '__main__':
    main()