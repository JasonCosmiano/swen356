from flask import Flask
from flask_restful import Resource, Api
from flask_cors import CORS

from api.db_utils import *

from api.user import User, SingleUser
from api.review import Review, SingleReview, Comments, Comment
from api.friend import Friend, FriendActivity, PotentialFriends

app = Flask(__name__) #create Flask instance
CORS(app) #Enable CORS on Flask server to work with Nodejs pages
api = Api(app) #api router

api.add_resource(User, '/user')
api.add_resource(SingleUser, '/user/<int:id>')
api.add_resource(Friend, '/friend/<int:id>')
api.add_resource(Review, '/review')
api.add_resource(SingleReview, '/review/<int:id>')
api.add_resource(Comments, '/comments/<int:id>')
api.add_resource(Comment, '/comment')
api.add_resource(FriendActivity, '/friendactivity/<int:id>')
api.add_resource(PotentialFriends, '/addfriends/<int:id>')


if __name__ == '__main__':
    
    print("Loading db")
    # sql file pending
    exec_sql_file('sql/tables.sql')
    print("Starting flask")
    app.run(debug=True), #starts Flask