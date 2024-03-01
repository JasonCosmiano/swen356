from flask import request

from flask_restful import Resource, reqparse
from .db_utils import *

class Friend(Resource):
    
    def get(self, id):
       """
       Get friends's list of a user
       """
       
       sql_command = """
            SELECT Users.username AS FRIEND_USERNAME, 
                  Users.user_id AS FRIEND_ID
            FROM Friends 
            INNER JOIN Users ON Users.user_id = Friends.friend_id 
            WHERE Friends.user_id = %(_id)s ;
      """
       result = exec_get_all_as_dict(sql_command, {'_id':id})
       
       if result == 0:
          return "USER DOES NOT EXIST"
       
       return result
    
    def post(self, id):
       """
       Follow a friend
       """
       # body params
       parser = reqparse.RequestParser()
       parser.add_argument('friend_id', type=str)
       
       args = parser.parse_args()
       friend_id = args['friend_id']

       if id == None or friend_id == None:
          return "INVALID REQUEST, MISSING PARAMETER"
       
       sql_command = """
            INSERT INTO Friends(user_id, friend_id)
            VALUES(%s, %s); 
        """
       result = exec_insert_update_delete(sql_command, (id, friend_id))

       if result == 0:
          return "FAILED TO FOLLOW FRIEND"

       return "FOLLOW FRIEND SUCCESS"    