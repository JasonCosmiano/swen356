from flask import request

from flask_restful import Resource, reqparse
from .db_utils import *

class User(Resource):

    def get(self):
       """
       Get all user's info
       Currently waiting on DB for sql command
       """

       sql_command = """SELECT * FROM Users;"""
       result = exec_get_all_as_dict(sql_command)
       return result
    
    def put(self):
       """Update with body params"""

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
       
       args = parser.parse_args()
       username = args['username']
       password = args['password']
       email = args['email']
       currentBook = args['currentBook']
                 
       # if statements
       
       # INSERT INTO statement, pending on DB
       sql_command = """
            INSERT INTO Users(username, password, email, currentBook)
            VALUES(%s, %s, %s, %s, %s, %s, %s)
        """
       result = exec_commit(sql_command, (username, password, email, currentBook))
       return result
    
       
class SingleUser(Resource):

   def get(self, id):
      """
      Get all user's info
      Currently waiting on DB for sql command
      """

      sql_command = """
         SELECT * 
         FROM Users 
         WHERE user_id = %(_id)s;
      """

      result = exec_commit(sql_command, {'_id':id}) # returns number of records

      if result == 0:
         return "USER DOES NOT EXIST"
      
      return result
   
   def delete(self, id):
      """
      Deletes a user based on id
      """    

      sql_command = """
      DELETE 
      FROM Users
      WHERE user_id = %d;
   """
      
      result = exec_commit(sql_command, id)
      return result