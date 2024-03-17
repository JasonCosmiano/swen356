from flask import request

from flask_restful import Resource, reqparse
from .db_utils import *

class BookInfo(Resource):
    def get(self, id):
        """
        Get details of a book
        """
        sql_command = """
            SELECT * FROM Books WHERE id = %(_id)s;
        """
        book = exec_get_all_as_dict(sql_command, {'_id':id})

        if book:
            return book
        else:
            return "Book not found"

    def post(self, id):
        """
        Add a review for the book
        """
        parser = reqparse.RequestParser()
        parser.add_argument('review_content', type=str, required=True)
        args = parser.parse_args()
        review_content = args['review_content']

        if not review_content:
            return "Review content missing"

        sql_command = """
            INSERT INTO Reviews(book_id, content)
            VALUES (%s, %s);
        """
        result = exec_insert_update_delete(sql_command, (id, review_content))

        if result:
            return "Review added successfully"
        else:
            return "Failed to add review"

class AddToReadingList(Resource):
    def post(self, id):
        """
        Add a book to the user's reading list
        """
        parser = reqparse.RequestParser()
        parser.add_argument('book_id', type=int, required=True)
        args = parser.parse_args()
        book_id = args['book_id']

        if not book_id:
            return "Book ID missing", 400

        sql_command = """
            INSERT INTO BookList(user_id, book_id)
            VALUES (%s, %s);
        """
        result = exec_insert_update_delete(sql_command, (id, book_id))

        if result:
            return "Book added to reading list successfully"
        else:
            return "Failed to add book to reading list"
        
class AllBooks(Resource):
    
    def get(self):
        """
        Get info off all books
        """
        sql_command = """ 
        SELECT title, genre, author, page_count, publisher, value, description
        FROM Books; """

        return exec_get_all_as_dict(sql_command, {'_id':id})
