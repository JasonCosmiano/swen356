from flask import request

from flask_restful import Resource, reqparse
from .db_utils import *

class Friend(Resource):
    
    def get(self, id):
       """
       Get friends's list of a user
       """
       
       # TODO need to do an inner join for usernames
       sql_command = """
            SELECT * 
            FROM Friends
            WHERE user_id = %(_id)s;"""
       result = exec_get_all_as_dict(sql_command, {'_id':id})
       
       if result == 0:
          return "USER DOES NOT EXIST"
       return result

class NewFriend(Resource):
    def post(self):
       """
       Send a friend request
       """
       # body params
       parser = reqparse.RequestParser()
       parser.add_argument('user_id', type=str)
       parser.add_argument('friend_id', type=str)
       
       args = parser.parse_args()
       user_id = args['user_id']
       friend_id = args['friend_id']

       if user_id == None or friend_id == None:
          return "INVALID REQUEST, MISSING PARAMETER"
       
       # 2 INSERT statements, for both people
       sql_command = """
            INSERT INTO Friends(user_id, friend_id)
            VALUES(%s, %s); 
        """
       exec_commit(sql_command, (user_id, friend_id))

       sql_command2 = """
            INSERT INTO Friends(friend_id, user_id)
            VALUES(%s, %s); 
        """
       result = exec_commit(sql_command2, (user_id, friend_id))

       return result