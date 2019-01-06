books = []

# TODO: Use database instead dummy book list

def existsBook(isbn):
    for book in books:
        if book["isbn"] == isbn:
            return book
    return None

def updateBook(isbn, newBook):
    #This is called if and only if the book with 'isbn' = isbn exists
    for book in books:
        if book["isbn"] == isbn:
            book.update(newBook)
            return book
    return None

def deleteBook(isbn):
    #This is called if and only if the book with 'isbn' = isbn exists
    i = 0
    for book in books:
        if book["isbn"] == isbn:
            books.pop(i)
            return book
        i = i + 1
    return None
