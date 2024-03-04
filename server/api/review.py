from flask import request

from flask_restful import Resource, reqparse
from .db_utils import *

class Review(Resource):


    def getAll(self):
       sql_command = """SELECT * FROM Review;"""
       result = exec_get_all_as_dict(sql_command)
       return result

    def getUserReviews(self):
       parser = reqparse.RequestParser()
       parser.add_argument('user_id', type=int)
       
       args = parser.parse_args()
       user_id = args['user_id']
       sql_command = """SELECT * FROM Review WHERE user_id = '%s';"""
       result = exec_get_all_as_dict(sql_command, (user_id))
       return result

    def getBookReviews(self):
       parser = reqparse.RequestParser()
       parser.add_argument('book_id', type=int)
       
       args = parser.parse_args()
       book_id = args['book_id']
       sql_command = """SELECT * FROM Review WHERE book_id = '%s';"""
       result = exec_get_all_as_dict(sql_command, (book_id))
       return result
    
    def put(self):
       # body params
       parser = reqparse.RequestParser()
       parser.add_argument('review_id', type=int)
       parser.add_argument('body', type=str)
       parser.add_argument('rating', type=int)
       
       args = parser.parse_args()
       review = args['review_id']
       body = args['body']
       rating = args['rating']
       
       # update statement, pending on DB
       if(rating != None and body != None):
         sql_command = """
            UPDATE Reviews SET body = '%s' AND rating = '%s' WHERE review_id = '%s'
         """
         result = exec_commit(sql_command, (body, rating, review_id))

       elif(rating == None):
         sql_command = """
            UPDATE Reviews SET body = '%s' WHERE review_id = '%s'
         """
         result = exec_commit(sql_command, (body, review_id))

       else:
         sql_command = """
            UPDATE Reviews SET rating = '%s' WHERE review_id = '%s'
         """
         result = exec_commit(sql_command, (rating, review_id))

         
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
       username = args['user_id']
       title = args['title']
       book_id = args['book_id']
       body = args['body']
       rating = args['rating']
       # if statements
       
       # INSERT INTO statement, pending on DB
       sql_command = """
            INSERT INTO Reviews(username, title, book_id, body, rating)
            VALUES(%s, %s, %s, %s, %s,)
        """
       result = exec_commit(sql_command, (username, title, book_id, body, rating))
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
       username = args['user_id']
       title = args['title']
       book_id = args['book_id']
       body = args['body']
       rating = args['rating']
       
       # INSERT INTO statement, pending on DB
       sql_command = """
            INSERT INTO Reviews(username, title, book_id, body, rating)
            VALUES(%s, %s, %s, %s, %s,)
        """
       result = exec_commit(sql_command, (username, title, book_id, body, rating))
       return result

class Comments(Resource):
   
    def getCommentsReview(self):
       parser = reqparse.RequestParser()
       parser.add_argument('review_id', type=int)
       args = parser.parse_args()
       review_id = args['review_id']

       sql_command = """SELECT * FROM Comments where review_id = '%s';"""
       result = exec_get_all_as_dict(sql_command,(review_id))
       return result
    
    def getCommentsUser(self):
       parser = reqparse.RequestParser()
       parser.add_argument('user_id', type=int)
       args = parser.parse_args()
       user_id = args['user_id']

       sql_command = """SELECT * FROM Comments where user_id = '%s';"""
       result = exec_get_all_as_dict(sql_command,(user_id))
       return result

    def put(self):
       # body params
       parser = reqparse.RequestParser()
       parser.add_argument('user_id', type=int)
       parser.add_argument('title', type=str)
       parser.add_argument('book_id', type=int)
       parser.add_argument('comment', type=str)
       parser.add_argument('rating', type=int)
       
       args = parser.parse_args()
       username = args['user_id']
       title = args['title']
       book_id = args['book_id']
       reply = args['reply']
       rating = args['rating']
       
       # update statement, pending on DB
       sql_command = """
        UPDATE Comments SET comment= '%s' WHERE review_id = '%s' and user_id = '%s'
        """
       result = exec_commit(sql_command, (reply, review_id, user_id))
       return result
    
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
            VALUES(%s, %s, %s, %s, %s,)
        """
       result = exec_commit(sql_command, (review_id, user_id, reply))
       return result

