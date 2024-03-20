from flask import Flask
from flask_restful import Resource, Api
from flask_cors import CORS

from api.db_utils import *
from api.load_books import *

from api.user import User, SingleUser
from api.review import Review, SingleReview, Comments, Comment
from api.bookinfo import BookInfo, AllBooks
from api.booklist import BookList, UserStats
from api.friend import Friend, FriendActivity, PotentialFriends
from api.reactions import Reactions

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
api.add_resource(BookInfo, '/book/<int:id>')
api.add_resource(BookList, '/booklist/<int:id>')
api.add_resource(FriendActivity, '/friendactivity/<int:id>')
api.add_resource(PotentialFriends, '/addfriends/<int:id>')
api.add_resource(Reactions, '/reactions')
api.add_resource(AllBooks, '/books')
api.add_resource(UserStats, '/userstats/<int:id>')


if __name__ == '__main__':
    
    print("Loading db")
    # sql file pending
    exec_sql_file('sql/tables.sql')
    # call load_books.py
    loadBooks()
    print("Starting flask")
    app.run(debug=True), #starts Flask