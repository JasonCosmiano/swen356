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
    
    def post(self):
       """POST with body params"""

       # body params
       parser = reqparse.RequestParser()
       parser.add_argument('username', type=str)
       parser.add_argument('password', type=str)
       parser.add_argument('email', type=str)
       parser.add_argument('currentBook', type=str)
       parser.add_argument('bookList', type=str)
       parser.add_argument('friendList', type=str)
       parser.add_argument('readingStats', type=str)
       
       args = parser.parse_args()
       username = args['username']
       password = args['password']
       email = args['email']
       currentBook = args['currentBook']
       bookList = args['bookList']
       friendList = args['friendList']
       readingStats = args['readingStats']
       
       # INSERT INTO statement, pending on DB
       sql_command = """
            INSERT INTO Users(username, password, email, currentBook, bookList, friendList, readingStats)
            VALUES(%s, %s, %s, %s, %s, %s, %s)
        """
       result = exec_commit(sql_command, (username, password, email, currentBook, bookList, friendList, readingStats))
       return result