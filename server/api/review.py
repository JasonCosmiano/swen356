from flask import request

from flask_restful import Resource, reqparse
from .db_utils import *

class Review(Resource):

    def get(self):
       sql_command = """SELECT * FROM Reviews;"""
       result = exec_get_all_as_dict(sql_command)
       return result
   
    
    def post(self):
       """POST with body params"""

       # body params
       parser = reqparse.RequestParser()
       parser.add_argument('user_id', type=int)
       parser.add_argument('title', type=str)
       parser.add_argument('book_id', type=int)
       parser.add_argument('body', type=str)
       parser.add_argument('rating', type=int)
       
       args = parser.parse_args()
       user_id = args['user_id']
       title = args['title']
       book_id = args['book_id']
       body = args['body']
       rating = args['rating']
       
       # INSERT INTO statement, pending on DB
       sql_command = """
            INSERT INTO Reviews(user_id, title, book_id, body, rating)
            VALUES(%s, %s, %s, %s, %s)
        """
       result = exec_insert_update_delete(sql_command, (user_id, title, book_id, body, rating))
       if result == 0:
          return "FAILED TO CREATE NEW REVIEW"
       
       return "POST SUCCESS"

class SingleReview(Resource):

    def get(self, id):

      sql_command = """
         SELECT * 
         FROM Reviews
         WHERE id = %(_id)s;
      """

      result = exec_get_all_as_dict(sql_command, {'_id':id}) # returns number of records

      if result == []:
         return "REVIEW DOES NOT EXIST"
      
      return result

    def put(self, id):
       # body params
       parser = reqparse.RequestParser()
       parser.add_argument('body', type=str)
       parser.add_argument('rating', type=int)
       
       args = parser.parse_args()
       body = args['body']
       rating = args['rating']
       
       # update statement, pending on DB
       if(rating != None and body != None):
         sql_command = """
            UPDATE Reviews SET body = %s, rating = %s WHERE id = %s
         """
         result = exec_insert_update_delete(sql_command, (body, rating, str(id)))

       elif(rating == None):
         sql_command = """
            UPDATE Reviews SET body = %s WHERE id = %s
         """
         result = exec_insert_update_delete(sql_command, (body, str(id)))

       else:
         sql_command = """
            UPDATE Reviews SET rating = %s WHERE id = %s
         """
         result = exec_insert_update_delete(sql_command, (rating, str(id)))
          
       if (result == 0):
            return "PUT command failed"
       
       return "PUT command success"
    
class ReviewUser(Resource):
    def get(self):
       parser = reqparse.RequestParser()
       parser.add_argument('user_id', type=int)
       
       args = parser.parse_args()
       user_id = args['user_id']
       sql_command = """SELECT * FROM Review WHERE user_id = %s;"""
       result = exec_get_all_as_dict(sql_command, (user_id))
       if(result == []):
         result = "USER REVIEWS DO NOT EXIST"
       return result

class ReviewBook(Resource):
    def get(self):
       parser = reqparse.RequestParser()
       parser.add_argument('book_id', type=int)
       
       args = parser.parse_args()
       book_id = args['book_id']
       sql_command = """SELECT * FROM Review WHERE book_id = %s;"""
       result = exec_get_all_as_dict(sql_command, (book_id))
       if(result == []):
         result = "BOOK REVIEWS DO NOT EXIST"
       return result

class Comments(Resource):
   
    def get(self, id):
       parser = reqparse.RequestParser()

       sql_command = """SELECT * FROM Comments where review_id = %s;"""
       result = exec_get_all_as_dict(sql_command,(str(id)))
       return result
    
class Comment(Resource):
    def post(self):
       """POST with body params"""

       # body params
       parser = reqparse.RequestParser()
       parser.add_argument('review_id', type=int)
       parser.add_argument('user_id', type=int)
       parser.add_argument('reply', type=str)
       
       args = parser.parse_args()
       review_id = args['review_id']
       user_id = args['user_id']
       reply = args['reply']
       # if statements
       
       # INSERT INTO statement, pending on DB
       sql_command = """
            INSERT INTO Comments(review_id,user_id, reply)
            VALUES(%s, %s, %s)
        """
       result = exec_insert_update_delete(sql_command, (review_id, user_id, reply))
       if result == 0:
          return "FAILED TO CREATE NEW COMMENT"
       
       return "POST SUCCESS"
