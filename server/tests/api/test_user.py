import unittest
from test_utils import *
from db.data import rebuild_tables
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
        print("TEST_GET_ALL_USERS PASS")