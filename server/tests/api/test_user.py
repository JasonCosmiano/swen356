import unittest

from server.tests.test_utils import *
from server.db.data import rebuild_tables
import json



class TestUser(unittest.TestCase):
    
    def setUp(self):
        """Rebuild tables before each test"""
        rebuild_tables()

    def test_get_user(self):
        """Unit test to get a specific user"""

        expected = 1
        actual = get_rest_call(self, 'http://localhost:5000/user/1') # invoke
        self.assertEqual(expected, len(actual)) # analyze
        print("TEST_GET_USER PASS")

    def test_get_nonexistent_user(self):
        """Unit test to get a user that does not exist"""
        expected = "USER DOES NOT EXIST"
        actual = get_rest_call(self, 'http://localhost:5000/user/15') # invoke
        self.assertEqual(expected, actual) # analyze
        print("TEST_GET_NONEXISTENT_USERS PASS")

    def test_post_new_user(self):
        """Add user"""
        print("\nTEST_POST_NEW_USER")

        # make new user
        _username = "Pedri"
        _password = "password123"
        _email = "moneymunson@rit.edu"
        _currentBook = "1"

        # body
        data = dict(username=_username, password=_password, email=_email, currentBook=_currentBook)
        jdata =json.dumps(data)
        print("TEST_POST_NEW_USER MAKING USER: ", jdata)

        #header
        hdr = {'content-type': 'application/json'}

        result = post_rest_call(self, "http://localhost:5000/user", jdata, hdr)
        self.assertEqual(result, "POST SUCCESS")  
        # print("TEST_POST_NEW_USER MAKING USER: ", result)
        print("TEST_POST_NEW_USER USER SUCCESSFULLY ADDED")


    def test_update_user(self):
        """Unit test to update a specific user"""
        
        print("\nTEST_PUT_USER")
    
        # edit user
        _username = "jumanji"
        _password = "password123"
        _email = "moneymunson@rit.edu"
        _currentBook = "2"

         # body
        data = dict(username=_username, password=_password, email=_email, currentBook=_currentBook)
        jdata =json.dumps(data)
        print("TEST_UPDATE_USER UPDATE USER WITH ID 1, WITH: " + str(data))

        #header
        hdr = {'content-type': 'application/json'}

        result = put_rest_call(self, "http://localhost:5000/user/1", jdata, hdr)
        self.assertEqual(result, "PUT command success")
        print("TEST_PUT_USER RESULT: ", str(result))