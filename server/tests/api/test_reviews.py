import unittest

from server.tests.test_utils import *
from server.db.data import rebuild_tables
import json



class TestUser(unittest.TestCase):
    
    def setUp(self):
        """Rebuild tables before each test"""
        rebuild_tables()

    def test_get_nonexistent_review(self):
        """Unit test to get a review that does not exist"""
        expected = "REVIEW DOES NOT EXIST"
        actual = get_rest_call(self, 'http://localhost:5000/review/15') # invoke
        self.assertEqual(expected, actual) # analyze
        print("TEST_GET_NONEXISTENT_REVIEW PASS")

    def test_post_new_review(self):
        """Add review"""
        print("\nTEST_POST_NEW_REVIEW")

        # make new review
        _userID = "3"
        _title = "My awesome review"
        _bookID = "1"
        _body = "Some text about the book"
        _rating = "4"

        # body
        data = dict(user_id=_userID, title=_title, book_id = _bookID, body=_body, rating=_rating)
        jdata =json.dumps(data)
        print("TEST_POST_NEW_REVIEW MAKING REVIEW: ", jdata)

        #header
        hdr = {'content-type': 'application/json'}

        result = post_rest_call(self, "http://localhost:5000/review", jdata, hdr)
        self.assertEqual(result, "POST SUCCESS")  
        print("TEST_POST_NEW_REVIEW REVIEW SUCCESSFULLY ADDED")


    def test_update_review(self):
        """Unit test to update a specific review"""
        
        print("\nTEST_PUT_REVIEW")
    
        # edit review
        _body = "Some text about the book"
        _rating = "5"

         # body
        data = dict(body=_body, rating=_rating)
        jdata =json.dumps(data)
        print("TEST_UPDATE_REVIEW UPDATE REVIEW WITH ID 1, WITH: " + str(data))

        #header
        hdr = {'content-type': 'application/json'}

        result = put_rest_call(self, "http://localhost:5000/review/1", jdata, hdr)
        self.assertEqual(result, "PUT command success")
        print("TEST_PUT_REVIEW RESULT: ", str(result))


    def test_post_new_comment(self):
        """Add review"""
        print("\nTEST_POST_NEW_REVIEW")

        # make new comment
        _reviewID = "1"
        _userID = "2"
        _reply = "This was terrible you are wrong"

        # body
        data = dict(review_id=_reviewID, user_id=_userID, reply = _reply)
        jdata =json.dumps(data)
        print("TEST_POST_NEW_COMMENT MAKING COMMENT: ", jdata)

        #header
        hdr = {'content-type': 'application/json'}

        result = post_rest_call(self, "http://localhost:5000/comment", jdata, hdr)
        self.assertEqual(result, "POST SUCCESS")  
        print("TEST_POST_NEW_COMMENT COMMENT SUCCESSFULLY ADDED")


