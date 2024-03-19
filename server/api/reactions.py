from flask import request

from flask_restful import Resource, reqparse
from .db_utils import *

class Reactions(Resource):
    def get(self):
        """
        gets reactions on a book
        """
        result = {}
        hearts = """
            SELECT COUNT(heart)
            FROM reactions
            WHERE heart = TRUE
            AND BookID = 1;
        """
        result['heart'] = exec_get_one(hearts)[0]

        thumbsUp = """
            SELECT COUNT(thumbsUp)
            FROM reactions
            WHERE thumbsUp = TRUE
            AND BookID = 1;
        """
        result['thumbsUp'] = exec_get_one(thumbsUp)[0]

        thumbsDown = """
            SELECT COUNT(thumbsDown)
            FROM reactions
            WHERE thumbsDown = TRUE
            AND BookID = 1;
        """
        result['thumbsDown'] = exec_get_one(thumbsDown)[0]

        crying = """
            SELECT COUNT(crying)
            FROM reactions
            WHERE crying = TRUE
            AND BookID = 1;
        """
        result['crying'] = exec_get_one(crying)[0]

        return result 
    
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('reaction', type=str)

        args = parser.parse_args()

        reaction = args['reaction']

        sql_command = """
            SELECT """ + reaction + """
            FROM reactions
            WHERE reactorID = 1
            AND BookID = 1;
        """

        status = exec_get_one(sql_command)

        if str(status[0]) == "True":
            resolution_command = """
                UPDATE reactions
                set  """ + reaction + """ = FALSE
                WHERE reactorid = 1
                AND bookid = 1; 
            """
        elif str(status[0]) == "False":
            resolution_command = """
                UPDATE reactions
                set  """ + reaction + """ = TRUE
                WHERE reactorid = 1
                AND bookid = 1; 
            """
        else:
            resolution_command = """
            SELECT COUNT( """ + reaction + """)
            FROM reactions
            WHERE  """ + reaction + """ = TRUE
            AND BookID = 1;
        """

        exec_insert_update_delete(resolution_command)

        result_command = """
            SELECT COUNT( """ + reaction + """)
            FROM reactions
            WHERE  """ + reaction + """ = TRUE
            AND BookID = 1;
        """

        result = exec_get_one(result_command)
        return str(result[0])