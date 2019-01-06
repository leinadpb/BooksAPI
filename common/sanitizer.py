def bookSanitize(book):
    if ("name" in book and "price" in book and "isbn" in book):
        return True
    else:
        return False