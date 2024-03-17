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
       
       if result == []:
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
    
class FriendActivity(Resource):
   
   def get(self, id):
      """
      Get friend's activity
      """
      sql_command = """
         SELECT friends.friend_id, users.username, books.id AS "book_id", books.title, books.genre, books.author 
         FROM books
         INNER JOIN booklist on booklist.bookid = books.id
		   INNER JOIN friends on friends.user_id = booklist.userid
		   INNER JOIN users ON users.user_id = friends.friend_id
         WHERE booklist.userid = %(_id)s;
      """

      result = exec_get_all_as_dict(sql_command, {'_id':id})
      return result

class PotentialFriends(Resource):

   def get(self, id):
      """
      Get potential new friends
      """
      sql_command = """
         SELECT  users.user_id
         FROM Users
         INNER JOIN friends on friends.user_id = users.user_id
         WHERE users.user_id = %(_id)s
         OR friends.friend_id = %(_id)s;
      """
      excluded_users = exec_get_all_as_dict(sql_command, {'_id':id}) # themselves and ppl they are already friends with
      excluded_list = str([d['user_id'] for d in excluded_users]).replace("[", "(").replace("]", ")")
      command = """
         SELECT * 
         FROM Users
         WHERE users.user_id NOT IN """ + excluded_list

      result = exec_get_all_as_dict(command)
      return result