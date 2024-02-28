from flask import request
from flask_restful import Resource, reqparse
from .db_utils import *

class login(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('username', type=str)
        parser.add_argument('password', type=str)
        args = parser.parse_args()
        result = login_user(args['username'], args['password'])
        return result
    
    def delete(self):
        # does NOT remove user from database
        return logout_user

""" 
Helper functions for login and logout
"""
def login_user(username, password):
    # head = request.headers
    # ^ this is in case password/username isn't passed directly into this metho
    sql_command = """
    SELECT password
    FROM Users 
    WHERE username = %s
    AND password = %s"""

    result = exec_get_one(sql_command, username, password)  
    if result == None:
        return "Invalid username or password. Try again"
    else:
        return "User " + username + " successfully logged in"
        
def logout_user():
    # may need to add functionality to stop 
    # displaying readinglist, friendlist
    # and other personal info here

    return "User successfully logged out"