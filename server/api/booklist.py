from flask import request

from flask_restful import Resource, reqparse
from .db_utils import *

class BookList(Resource):
    def get(self, id):
        sql_command = """
        SELECT Books.title AS BOOK_TITLE,
                  Books.genre AS GENRE,
                  Books.author AS AUTHOR,
                  Books.page_count AS PAGE_COUNT
            FROM BookList 
            INNER JOIN Books ON Books.id = BookList.bookID 
            WHERE BookList.userID = %(_id)s;
        """

        result = exec_get_all_as_dict(sql_command, {'_id':id})

        if not result:
            return "USER DOES NOT EXIST"

        return result

    def post(self, id):
        parser = reqparse.RequestParser()
        parser.add_argument('book_id', type=int, required=True)
        args = parser.parse_args()
        book_id = args['book_id']

        if not id or not book_id:
            return "INVALID REQUEST, MISSING PARAMETER"

        sql_command = """
            INSERT INTO BookList(userID, bookID)
            VALUES (%s, %s);
        """
        result = exec_insert_update_delete(sql_command, (id, book_id))

        if result == 0:
            return "FAILED TO ADD BOOK TO BOOKLIST"

        return "BOOK ADDED TO BOOKLIST SUCCESSFULLY"

    def delete(selfd, id):
        parser = reqparse.RequestParser()
        parser.add_argument('book_id', type=int, required=True)
        args = parser.parse_args()
        book_id = args['book_id']

        if not id or not book_id:
            return "INVALID REQUEST, MISSING PARAMETER"

        sql_command = """
            DELETE FROM BookList
            WHERE userID = %s AND bookID = %s;
        """
        result = exec_insert_update_delete(sql_command, (id, book_id))

        if result == 0:
            return "FAILED TO REMOVE BOOK FROM BOOKLIST"

        return "BOOK REMOVED FROM BOOKLIST SUCCESSFULLY"

    def filter(self):
        """
        Filter the user's booklist by genre, author, and length
        """
        parser = reqparse.RequestParser()
        parser.add_argument('genre', type=str)
        parser.add_argument('author', type=str)
        parser.add_argument('min_length', type=int)
        args = parser.parse_args()
        genre = args.get('genre')
        author = args.get('author')
        min_length = args.get('min_length')

        sql_command = """
            SELECT Books.title AS BOOK_TITLE,
                  Books.genre AS GENRE,
                  Books.author AS AUTHOR,
                  Books.page_count AS PAGE_COUNT,
            FROM BookList 
            INNER JOIN Books ON Books.id = BookList.bookID 
            WHERE BookList.userID = %s
        """
        params = [id]

        if genre:
            sql_command += " AND Books.genre = %s"
            params.append(genre)
        if author:
            sql_command += " AND Books.author = %s"
            params.append(author)
        if min_length:
            sql_command += " AND Books.page_count >= %s"
            params.append(min_length)

        result = exec_get_all_as_dict(sql_command, tuple(params))

        if not result:
            return "NO BOOKS FOUND FOR THE GIVEN FILTER CRITERIA"

        return result