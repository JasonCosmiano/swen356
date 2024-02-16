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
       parser.add_argument('user_id', type=str)
       
       args = parser.parse_args()
       username = args['username']
       password = args['password']
       email = args['email']
       currentBook = args['currentBook'] 
       user_id = args['user_id'] 

       # init messages
       message = "PUT command falied"
       a_dict = {'message':message} 

       # only update username
       if password == None and email == None and currentBook == None:
          sql_command = """
                UPDATE User 
                SET username=%s
                WHERE user_id=%s
            """
          result = exec_commit(sql_command, (username, user_id))

      # only update password
       elif username == None and email == None and currentBook == None:
          sql_command = """
                UPDATE User 
                SET password=%s
                WHERE user_id=%s
            """
          result = exec_commit(sql_command, (password, user_id))

      # only email 
       elif username == None and password == None and currentBook == None:
          sql_command = """
                UPDATE User 
                SET email=%s
                WHERE user_id=%s
            """
          result = exec_commit(sql_command, (password, user_id))

      # only currentBook password
       elif username == None and password == None and email == None:
          sql_command = """
                UPDATE User 
                SET currentBook=%s
                WHERE user_id=%s
            """
          result = exec_commit(sql_command, (password, user_id))

      # only username, password, email
       elif currentBook == None:
          sql_command = """
                UPDATE User 
                SET username=%s, password=%s, email=%s
                WHERE user_id=%s
            """
          result = exec_commit(sql_command, (username, password, email, user_id))

      # only currentBook, password, email
       elif username == None:
          sql_command = """
                UPDATE User 
                SET currentBook=%s, password=%s, email=%s
                WHERE user_id=%s
            """
          result = exec_commit(sql_command, (currentBook, password, email, user_id))


      # only currentBook, password, username
       elif email == None:
          sql_command = """
                UPDATE User 
                SET currentBook=%s, password=%s, username=%s
                WHERE user_id=%s
            """
          result = exec_commit(sql_command, (currentBook, password, username, user_id))

      # only currentBook, email, username
       elif password == None:
          sql_command = """
                UPDATE User 
                SET currentBook=%s, email=%s, username=%s
                WHERE user_id=%s
            """
          result = exec_commit(sql_command, (currentBook, email, username, user_id))

      # only email, username
       elif password == None and currentBook == None:
          sql_command = """
                UPDATE User 
                SET username=%s, email=%s
                WHERE user_id=%s
            """
          result = exec_commit(sql_command, (username, email, user_id))

      # only password, username
       elif email == None and currentBook == None:
          sql_command = """
                UPDATE User 
                SET username=%s, password=%s
                WHERE user_id=%s
            """
          result = exec_commit(sql_command, (username, password, user_id))

      # only currentBook, username
       elif email == None and password == None:
          sql_command = """
                UPDATE User 
                SET username=%s, currentBook=%s
                WHERE user_id=%s
            """
          result = exec_commit(sql_command, (username, currentBook, user_id))
      
      # only password, currentBook
       elif username == None and email == None:
          sql_command = """
                UPDATE User 
                SET password=%s, currentBook=%s
                WHERE user_id=%s
            """
          result = exec_commit(sql_command, (password, currentBook, user_id))
   
      # only password, email
       elif username == None and currentBook == None:
          sql_command = """
                UPDATE User 
                SET password=%s, email=%s
                WHERE user_id=%s
            """
          result = exec_commit(sql_command, (password, email, user_id))

      # only currentBook, email
       elif username == None and password == None:
          sql_command = """
                UPDATE User 
                SET currentBook=%s, email=%s
                WHERE user_id=%s
            """
          result = exec_commit(sql_command, (currentBook, email, user_id))

      # update everything
       else:
          sql_command = """
                UPDATE User 
                SET currentBook=%s, email=%s, password=%s, username=%s
                WHERE user_id=%s
            """
          result = exec_commit(sql_command, (currentBook, email, password, username, user_id))

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
    