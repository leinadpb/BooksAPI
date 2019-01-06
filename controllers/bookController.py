from common.common_imports import *

def bookController(app, Book):
    #GET /books
    @app.route('/books') 
    def getBooksRoute():
        try:
            result = Book.get_all()
            if not result:
                response = Response(json.dumps(notFound), status=404, mimetype="application/json")
            else:
                fetchSuccess["data"] = result
                fetchSuccess["totalRows"] = len(result)
                response = Response(json.dumps(fetchSuccess), status=200, mimetype="application/json")
        except:
            response = Response(json.dumps(invalidRequest), status=400, mimetype="application/json")

        return response

    #GET /books/{id}
    @app.route('/books/<int:isbn>')
    def getBookRoute(isbn):
        try:
            result = Book.getByIsbn(isbn)
            if not result:
                response = Response(json.dumps(notFound), status=404, mimetype="application/json")
            else:
                fetchSuccess["data"] = result
                fetchSuccess["totalRows"] = 1
                response = Response(json.dumps(fetchSuccess), status=200, mimetype="application/json")
        except:
            response = Response(json.dumps(invalidRequest), status=400, mimetype="application/json")

        return response

    #POST /book
    @app.route('/books', methods=['POST'])
    def addBookRoute():
        data = request.get_json()
        if bookSanitize(data):
            try:
                result = Book.add_book(data)
                createdObject["data"] = result
                response = Response(json.dumps(createdObject), status=201, mimetype="application/json")
                response.headers['Location'] = "/books/" + str(result['isbn'])
            except:
                response = Response(json.dumps(invalidOperation), status=500, mimetype="application/json")
        else:
            response = Response(json.dumps(invalidRequest), status=400, mimetype="application/json")

        return response

    #PUT /books/{id}
    @app.route('/books/<int:isbn>', methods=['PUT'])
    def updateBookRoute(isbn):
        try:
            existing_book = Book.getByIsbn(isbn)
            if existing_book is not None:
                meta_data = request.get_json()
                result = Book.updateBook(existing_book, meta_data)

                updatedObject["data"] = result
                response = Response(json.dumps(updatedObject), status=204, mimetype="application/json")
                response.headers["Location"] = "/books/" + str(isbn)
            else:
                response = Response(json.dumps(notFound), status=404, mimetype="application/json")
        except:
            response = Response(json.dumps(invalidOperation), status=500, mimetype="application/json")

        return response

    #DELETE /books/{id}
    @app.route('/books/<int:isbn>', methods=['DELETE'])
    def deleteBookRoute(isbn):
        try:
            book = Book.getByIsbn(isbn)
            if book is not None:
                Book.deleteByIsbn(isbn)
                deletedObject["data"] = book
                response = Response(json.dumps(deletedObject), status=204, mimetype="application/json")
            else:
                response = Response(json.dumps(notFound), status=404, mimetype="application/json")
        except:
            response = Response(json.dumps(invalidOperation), status=500, mimetype="application/json") 

        return response
