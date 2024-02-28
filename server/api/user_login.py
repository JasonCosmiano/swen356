from flask import request
from flask_restful import Resource, reqparse
from .db_utils import *

class user_login:
    current_user = None

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
            current_user = username
            return "User " + username + " sueccessfully logged in!"
        
    def logout_user():
        # may need to add functionality to stop 
        # displaying readinglist, friendlist
        # and other personal info here

        current_user = None
        return "User successfully logged out"