from common.common_imports import *

def authorController(app, author):

    @app.route('/authors')
    def main_route():
       return "It's working!"