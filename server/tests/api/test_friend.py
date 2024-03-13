import unittest

from server.tests.test_utils import *
from server.db.data import rebuild_tables
import json



class TestFriend(unittest.TestCase):
    
    def setUp(self):
        """Rebuild tables before each test"""
        rebuild_tables()

    def test_get_friends(self):
        """Unit test to get friends of a specific user"""
        expected = 1
        actual = get_rest_call(self, 'http://localhost:5000/friend/1') # invoke
        self.assertEqual(expected, len(actual)) # analyze
        print("TEST_GET_FRIEND PASS")

    def test_get_friend_nonexistent(self):
        """Unit test to get friend of nonexistent user"""
        actual = get_rest_call(self, 'http://localhost:5000/friend/100') # invoke
        self.assertEqual("USER DOES NOT EXIST", actual) # analyze
        print("TEST_GET_FRIEND_NONEXISTENT PASS")

    def test_post_friends(self):
        """ Add a friend """
        print("\nTEST_POST_NEW_USER")

        # make new user
        _friend_id = "3"

        # body
        data = dict(friend_id=_friend_id)
        jdata =json.dumps(data)
        print("test_post_friends following a friend: ", jdata)

        #header
        hdr = {'content-type': 'application/json'}

        result = post_rest_call(self, "http://localhost:5000/friend/1", jdata, hdr)
        self.assertEqual(result, "FOLLOW FRIEND SUCCESS") 

    
