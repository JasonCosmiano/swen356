from flask import request

from flask_restful import Resource, reqparse
from .db_utils import *

class User(Resource):


    def get(self):
       """
       Get a user's info
       Currently waiting on DB for sql command
       """

       sql_command = """SELECT * FROM Users;"""
       result = exec_get_all_as_dict(sql_command)
       return result
    
    def put(self):
       """Update with body params"""

       # body params
       parser = reqparse.RequestParser()
       parser.add_argument('currentBook', type=str)
       parser.add_argument('bookList', type=str)
       parser.add_argument('friendList', type=str)
       parser.add_argument('readingStats', type=str)
       
       args = parser.parse_args()
       currentBook = args['currentBook']
       bookList = args['bookList']
       friendList = args['friendList']
       readingStats = args['readingStats']
       
       # update statement, pending on DB
       sql_command = """
        """
       result = exec_commit(sql_command, (currentBook, bookList, friendList, readingStats))
       return result
    
class CreateUser(Resource):
    def post(self):
       """POST with body params"""

       # body params
       parser = reqparse.RequestParser()
       parser.add_argument('currentBook', type=str)
       parser.add_argument('bookList', type=str)
       parser.add_argument('friendList', type=str)
       parser.add_argument('readingStats', type=str)
       
       args = parser.parse_args()
       currentBook = args['currentBook']
       bookList = args['bookList']
       friendList = args['friendList']
       readingStats = args['readingStats']
       
       # INSERT INTO statement, pending on DB
       sql_command = """
        """
       result = exec_commit(sql_command, (currentBook, bookList, friendList, readingStats))
       return result